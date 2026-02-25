import asyncio
import aiohttp
import time
import xmltodict

BASE_URL = "http://192.168.0.195/mux_http"

# All known MC parameters (we will refine this list)
ALL_PARAMS = [
    "D_Y_6", "D_Y_7", "D_C_1_1",
    "D_A_1_7", "D_A_1_8", "D_A_1_9",
    "D_D_1", "D_D_2", "D_D_3",
    "D_A_2_1", "D_A_2_2", "D_A_2_3",
]

async def fetch_show(session, params):
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


async def test_param(session, param):
    print(f"\nTesting: {param}")
    status, text, elapsed = await fetch_show(session, [param])

    if status is None:
        print(f"❌ FAIL: {text}")
        return False

    if not text.strip():
        print("❌ FAIL: Empty response")
        return False

    try:
        parsed = xmltodict.parse(text)
        print(f"✔ OK: {parsed}")
        return True
    except Exception as e:
        print(f"❌ XML Parse Error: {e}")
        print(f"Raw: {text}")
        return False


async def main():
    supported = []
    unsupported = []

    async with aiohttp.ClientSession() as session:
        for param in ALL_PARAMS:
            ok = await test_param(session, param)
            if ok:
                supported.append(param)
            else:
                unsupported.append(param)

    print("\n=== SUMMARY ===")
    print("Supported:", supported)
    print("Unsupported:", unsupported)


if __name__ == "__main__":
    asyncio.run(main())
