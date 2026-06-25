import aiohttp
import asyncio
import base64
import re
import logging
import time
import datetime
import xmltodict
from aiohttp import ClientSession, ClientTimeout, ServerDisconnectedError

from .parameter_map import PARAMETERS  # adjust import if needed

_LOGGER = logging.getLogger(__name__)


class GruenbeckMC:
    """
    Python client for Grünbeck softliQ:MC Webservice.
    Supports:
      - show=PARAM
      - edit=PARAM>VALUE
      - code=XXX
      - Base64 encoding for protected parameters
    """

    @staticmethod
    async def create(host: str, session: ClientSession | None = None):
        """Factory method used by Home Assistant to create the client.

        `session` is optional; when a session is provided it is owned by
        the caller (Home Assistant) and MUST NOT be closed by this client.
        If no session is provided, the client will create and own its own
        `aiohttp.ClientSession` which will be closed on `close()`.
        """
        client = GruenbeckMC(host, session)
        await client._init()
        return client

    def __init__(self, host: str, session: ClientSession | None = None, request_interval_ms: int = 20):
        # Accept a None session for standalone usage; create our own in that case
        self.host = host
        if session is None:
            # We create a dedicated ClientSession and mark ownership so we
            # can safely close it later. Import here to avoid top-level
            # dependency issues in Home Assistant.
            self.session = aiohttp.ClientSession()
            self._own_session = True
        else:
            self.session = session
            self._own_session = False
        self.last_request = 0
        self.request_interval = request_interval_ms / 1000.0
        self.connected = False
        self._lock = asyncio.Lock()

    async def _init(self):
        """Test connectivity by requesting a harmless parameter.
            D_Y_6 = Software Version of the device
        """
        try:
            resp = await self.get_param("D_Y_6")
            # If the device returns valid XML, we consider it connected
            self.connected = "error" not in resp
        except Exception:
            self.connected = False
            raise


    async def close(self):
        """Close the aiohttp session if we created it."""
        # Only close sessions that this client created to avoid closing
        # Home Assistant's shared aiohttp session.
        if getattr(self, "_own_session", False):
            if self.session and not self.session.closed:
                await self.session.close()

    async def _throttle(self):
        now = time.monotonic()
        delta = now - self.last_request
        if delta < self.request_interval:
            await asyncio.sleep(self.request_interval - delta)
        self.last_request = time.monotonic()

    async def _post(self, payload: str):
        """Send POST request to /mux_http."""
        async with self._lock:
            await self._throttle()

            url = f"http://{self.host}/mux_http"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}

            async with self.session.post(url, data=payload, headers=headers) as resp:
                text = await resp.text()
                try:
                    return xmltodict.parse(text)
                except Exception:
                    return {"error": "invalid_xml", "raw": text}

    def _process_value(self, param: str, value: str):
        """Apply parameter_map transformations (dict mapping + base64 decoding)."""

        meta = PARAMETERS.get(param)
        if not meta:
            return value

        # Base64 decoding (if required)
        if meta.get("base64") and value:
            try:
                value = base64.b64decode(value).decode("utf-8")
            except Exception:
                _LOGGER.debug("_process_value: failed to base64-decode param %s value=%r", param, value)
                return value  # fail silently, or log if desired

        # Dict translation (if defined)
        mapping = meta.get("dict")
        if mapping:
            return mapping.get(str(value), value)

        # If parameter is declared as numeric, try to coerce to a Python number.
        # Some device values include their unit (e.g. "0.0l") which must be
        # stripped before conversion — extract the first numeric substring.
        ptype = meta.get("type")
        if ptype and isinstance(ptype, str) and ptype.lower() == "number":
            # If it's already numeric, return as-is
            if isinstance(value, (int, float)):
                return value

            if isinstance(value, str):
                # Normalize comma decimals to dot
                v = value.strip().replace(",", ".")
                m = re.search(r"[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?", v)
                if m:
                    num_str = m.group(0)
                    try:
                        # Prefer int when there's no decimal point
                        if "." in num_str or "e" in num_str.lower():
                            return float(num_str)
                        return int(num_str)
                    except Exception:
                        _LOGGER.debug("_process_value: numeric parse error for %s value=%r", param, value)
                        # Fall through and return original string on parse error
                        return value
                else:
                    _LOGGER.debug("_process_value: no numeric substring found for %s value=%r", param, value)
                    return value

        # Date/time cleanup: strip German 'Uhr' suffix from datetime strings
        # when the parameter unit indicates a date or time value or when the
        # parameter is a timestamp device class.
        unit = meta.get("unit")
        device_class = meta.get("device_class")
        if isinstance(value, str) and (
            (isinstance(unit, str) and ("date" in unit.lower() or "time" in unit.lower()))
            or (isinstance(device_class, str) and device_class.lower() == "timestamp")
        ):
            try:
                value = re.sub(r"\s*Uhr\s*$", "", value, flags=re.IGNORECASE).strip()
                dt = datetime.strptime(value, "%d.%m.%Y %H:%M")
                value = dt.isoformat()
            except Exception:
                # Non-fatal: leave original value on any unexpected error
                pass

        return value

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    async def get_param(self, param: str, code: str | None = None):
        """
        Read a single parameter.
        Example:
            await client.get_param("D_D_1")
            await client.get_param("D_A_1_1", code="005")
        """
        if code:
            payload = f"id=1234&code={code}&show={param}~"
        else:
            payload = f"id=1234&show={param}~"

        #return await self._post(payload)
        data = await self._post(payload)

        # If the lower-level _post returned a {'data': {param: value, ...}}
        # mapping (some code paths/tools produce this shape), prefer that
        # and apply processing (base64 decode / mapping) to the value.
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict):
            if param in data["data"]:
                return self._process_value(param, data["data"][param])
            # param not present — log raw response and return it so caller can inspect
            _LOGGER.debug("get_param: param %s not present in data response, returning raw response: %s", param, data)
            return data

        try:
            value = data["root"]["param"]["value"]  # adjust to real XML structure
            return self._process_value(param, value)
        except Exception:
            _LOGGER.debug("get_param: unexpected response structure for %s: %s", param, data)
            return data

    async def get_params(self, params: list[str], code: str | None = None):
        """
        Read multiple parameters.
        """
        show = "|".join(params)

        if code:
            payload = f"id=1234&code={code}&show={show}~"
        else:
            payload = f"id=1234&show={show}~"

        #return await self._post(payload)
        data = await self._post(payload)

        # If we get {'data': {param: value, ...}} use that and process values
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict):
            processed = {}
            for p, v in data["data"].items():
                processed[p] = self._process_value(p, v)
            return processed

        processed = {}
        try:
            returned_params = data["root"]["param"]  # adjust to real structure

            if not isinstance(returned_params, list):
                returned_params = [returned_params]

            for item in returned_params:
                param_name = item["name"]
                value = item["value"]
                processed[param_name] = self._process_value(param_name, value)

            return processed

        except Exception:
            _LOGGER.debug("get_params: unexpected response structure for params %s: %s", params, data)
            return data

    async def set_param(self, param: str, value: str, code: str | None = None, base64_encode=False):
        """
        Write a parameter.
        Example:
            await client.set_param("D_D_1", "20")
            await client.set_param("D_Y_8_4", "myuser", base64_encode=True)
        """
        if base64_encode:
            value = base64.b64encode(value.encode("utf-8")).decode("utf-8")

        if code:
            payload = f"id=1234&code={code}&edit={param}>{value}&show={param}~"
        else:
            payload = f"id=1234&edit={param}>{value}&show={param}~"

        return await self._post(payload)