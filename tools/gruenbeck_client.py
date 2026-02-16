import aiohttp
import asyncio
import xmltodict

class GruenbeckClient:
    def __init__(self, host: str):
        self.host = host
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    async def fetch(self, params: str):
        """Send POST request to /mux_http and return parsed XML."""
        url = f"http://{self.host}/mux_http"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        async with self.session.post(url, data=params, headers=headers) as resp:
            text = await resp.text()
            return xmltodict.parse(text)

    async def get_basic_info(self):
        """
        Equivalent to JS:
        getXML("id=<id>&show=D_Y_6|D_Y_7|D_C_1_1~", 1)
        """
        params = "id=1234&show=D_Y_6|D_Y_7|D_C_1_1~"
        return await self.fetch(params)


async def main():
    client = GruenbeckClient("192.168.0.195")

    print("Henter basisdata...")
    data = await client.get_basic_info()

    print("\n=== RAW XML PARSED ===")
    print(data)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
