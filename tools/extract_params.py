import re
import aiohttp
import asyncio

HOST = "192.168.0.195"

async def fetch_js():
    url = f"http://{HOST}/gruenbeck.js"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

def extract_parameters(js_text):
    # Find alle forekomster af: parameter: "D_X_1_1"
    pattern = r'parameter\s*:\s*"([A-Z]_[A-Z0-9_]+)"'
    return sorted(set(re.findall(pattern, js_text)))

async def main():
    print("Henter gruenbeck.js...")
    js = await fetch_js()

    print("Parser parametre...")
    params = extract_parameters(js)

    print(f"Fundet {len(params)} parametre:")
    for p in params:
        print("  ", p)

    # Gem til fil
    with open("softliq_params.txt", "w") as f:
        for p in params:
            f.write(p + "\n")

    print("\nParametre gemt i softliq_params.txt")

asyncio.run(main())
