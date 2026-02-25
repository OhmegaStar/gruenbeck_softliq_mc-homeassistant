import asyncio
import aiohttp
import time

BASE_URL = "http://192.168.0.195/mux_http"

async def post_raw(session, body):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        start = time.perf_counter()
        async with session.post(BASE_URL, data=body, headers=headers, timeout=10) as resp:
            text = await resp.text()
            elapsed = time.perf_counter() - start
            return text, elapsed, resp.status
    except Exception as e:
        return f"ERROR: {e}", None, None


async def test_single():
    print("\n=== SINGLE PARAM TEST ===")
    body = "code=000&show=D_A_1_7"
    async with aiohttp.ClientSession() as session:
        text, elapsed, status = await post_raw(session, body)
        print(f"Body: {body}")
        print(f"Status: {status}")
        print(f"Time: {elapsed:.3f}s" if elapsed else "Timeout/Error")
        print(f"Response:\n{text}")

async def test_multi():
    print("\n=== MULTI PARAM TEST ===")
    body = "code=000&show=D_A_1_7|D_A_1_8|D_A_1_9"
    async with aiohttp.ClientSession() as session:
        text, elapsed, status = await post_raw(session, body)
        print(f"Body: {body}")
        print(f"Status: {status}")
        print(f"Time: {elapsed:.3f}s" if elapsed else "Timeout/Error")
        print(f"Response:\n{text}")

async def main():
    await test_single()
    await test_multi()

if __name__ == "__main__":
    asyncio.run(main())
