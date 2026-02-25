import asyncio
import aiohttp
import time
import xmltodict

BASE_URL = "http://192.168.0.195/mux_http"

# Generate a full list of known Grünbeck parameters
PARAM_GROUPS = {
    "D_A": [(1, 1, 20), (2, 1, 20), (3, 1, 20)],
    "D_D": [(1, 1, 20)],
    "D_C": [(1, 1, 20)],
    "D_Y": [(1, 1, 20)],
    "P_A": [(1, 1, 20)],
    "P_C": [(1, 1, 20)],
    "P_D": [(1, 1, 20)],
    "P_Y": [(1, 1, 20)],
}

def generate_params():
    params = []
    for prefix, ranges in PARAM_GROUPS.items():
        for group, start, end in ranges:
            for i in range(start, end + 1):
                params.append(f"{prefix}_{group}_{i}")
    return params

ALL_PARAMS = generate_params()

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
    status, text, elapsed = await fetch_show(session, [param])

    if status is None:
        return param, False, f"ERROR: {text}"

    if not text.strip():
        return param, False, "Empty response"

    try:
        parsed = xmltodict.parse(text)
        return param, True, parsed["data"]
    except Exception as e:
        return param, False, f"XML error: {e}"

async def main():
    supported = {}
    unsupported = {}

    async with aiohttp.ClientSession() as session:
        for param in ALL_PARAMS:
            name, ok, result = await test_param(session, param)
            if ok:
                supported[name] = result
            else:
                unsupported[name] = result

    print("\n=== SUPPORTED PARAMETERS ===")
    for k, v in supported.items():
        print(f"{k}: {v}")

    print("\n=== UNSUPPORTED PARAMETERS ===")
    for k, v in unsupported.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    asyncio.run(main())
