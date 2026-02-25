import aiohttp
import asyncio
import base64
import time
import xmltodict
from aiohttp import ClientSession, ClientTimeout, ServerDisconnectedError

from .parameter_map import PARAMETERS  # adjust import if needed


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
    async def create(host: str, session: ClientSession):
        """Factory method used by Home Assistant to create the client."""
        client = GruenbeckMC(host, session)
        await client._init()
        return client

    def __init__(self, host: str, session: ClientSession, request_interval: int = 1):
        self.host = host
        self.session = session
        self.last_request = 0
        self.request_interval = request_interval
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
                return value  # fail silently, or log if desired

        # Dict translation (if defined)
        mapping = meta.get("dict")
        if mapping:
            return mapping.get(str(value), value)

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

        try:
            value = data["root"]["param"]["value"]  # adjust to real XML structure
            return self._process_value(param, value)
        except Exception:
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