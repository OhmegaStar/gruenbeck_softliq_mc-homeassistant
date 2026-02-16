import aiohttp
import asyncio
import base64
import time
import xmltodict


class GruenbeckMC:
    """
    Python client for Grünbeck softliQ:MC Webservice.
    Supports:
      - show=PARAM
      - edit=PARAM>VALUE
      - code=XXX
      - Base64 encoding for protected parameters
    """

    def __init__(self, host: str, request_interval: int = 15):
        self.host = host
        self.session = None
        self.last_request = 0
        self.request_interval = request_interval  # recommended: 15 seconds

    async def _ensure_session(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()

    async def _throttle(self):
        """Ensure minimum delay between requests."""
        now = time.time()
        delta = now - self.last_request
        if delta < self.request_interval:
            await asyncio.sleep(self.request_interval - delta)
        self.last_request = time.time()

    async def _post(self, payload: str):
        """Send POST request to /mux_http."""
        await self._ensure_session()
        await self._throttle()

        url = f"http://{self.host}/mux_http"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        async with self.session.post(url, data=payload, headers=headers) as resp:
            text = await resp.text()
            try:
                return xmltodict.parse(text)
            except Exception:
                return {"error": "invalid_xml", "raw": text}

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
        payload = f"id=1234&show={param}~"
        if code:
            payload = f"id=1234&show={param}&code={code}~"
        return await self._post(payload)

    async def get_params(self, params: list[str], code: str | None = None):
        """
        Read multiple parameters.
        """
        show = "|".join(params)
        payload = f"id=1234&show={show}~"
        if code:
            payload = f"id=1234&show={show}&code={code}~"
        return await self._post(payload)

    async def set_param(self, param: str, value: str, code: str | None = None, base64_encode=False):
        """
        Write a parameter.
        Example:
            await client.set_param("D_D_1", "20")
            await client.set_param("D_Y_8_4", "myuser", base64_encode=True)
        """
        if base64_encode:
            value = base64.b64encode(value.encode("utf-8")).decode("utf-8")

        payload = f"id=1234&edit={param}>{value}&show={param}~"
        if code:
            payload = f"id=1234&edit={param}>{value}&show={param}&code={code}~"

        return await self._post(payload)
