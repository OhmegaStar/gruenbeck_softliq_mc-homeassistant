import re
import aiohttp
import asyncio

HOST = "192.168.0.195"

async def fetch_js():
    url = f"http://{HOST}/gruenbeck.js"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

def extract_tags(js_text):
    # Look for getElementsByTagName("D_X_1_1")
    pattern = r'getElementsByTagName\("([A-Z]_[A-Z0-9_]+)"\)'
    tags = re.findall(pattern, js_text)
    return sorted(set(tags))

async def main():
    print("Fetching gruenbeck.js...")
    js = await fetch_js()

    print("Extracting XML tag names...")
    tags = extract_tags(js)

    print(f"Found {len(tags)} tags:")
    for t in tags:
        print("  ", t)

    with open("softliq_tags.txt", "w") as f:
        for t in tags:
            f.write(t + "\n")

    print("\nSaved to softliq_tags.txt")

asyncio.run(main())
