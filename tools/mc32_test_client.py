import asyncio
import aiohttp
import time
import xmltodict

BASE_URL = "http://192.168.0.195/mux_http"

# Example parameter sets to test
TEST_SETS = {
    "basic_info": ["D_Y_6", "D_Y_7", "D_C_1_1"],
    "date_time": ["D_A_1_7", "D_A_1_8", "D_A_1_9"],
    "device_status": ["D_D_1", "D_D_2", "D_D_3"],
    "water_usage": ["D_A_2_1", "D_A_2_2", "D_A_2_3"],
}

async def fetch_show(session, params):
    """
    Send a POST request using the MC32 'show' API:
    id=<id>&show=PARAM1|PARAM2|...~
    """
    show = "|".join(params) + "~"
    body = f"id=1234&show={show}"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0",
    }

    try:
        start = time.perf_counter()
        async with session.post(BASE_URL, data=body, headers=headers, timeout=10) as resp:
            text = await resp.text()
            elapsed = time.perf_counter() - start
            return resp.status, text, elapsed
    except Exception as e:
        return None, f"ERROR: {e}", None


async def test_param_set(session, name, params):
    print(f"\n=== TEST: {name} ===")
    print(f"Params: {params}")

    status, text, elapsed = await fetch_show(session, params)

    if status is None:
        print(f"Error: {text}")
        return

    print(f"HTTP Status: {status}")
    print(f"Time: {elapsed:.3f}s")

    if not text.strip():
        print("Empty response (device rejected request)")
        return

    try:
        parsed = xmltodict.parse(text)
        print("Parsed XML:")
        print(parsed)
    except Exception as e:
        print(f"XML Parse Error: {e}")
        print("Raw response:")
        print(text)


async def main():
    async with aiohttp.ClientSession() as session:
        for name, params in TEST_SETS.items():
            await test_param_set(session, name, params)


if __name__ == "__main__":
    asyncio.run(main())
