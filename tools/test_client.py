import asyncio
from gruenbeck_mc import GruenbeckMC

async def main():
    client = GruenbeckMC("192.168.0.195")

    print("Reading raw water hardness (D_D_1)...")
    print(await client.get_param("D_D_1"))

    print("Reading soft water hardness target (D_D_2)...")
    print(await client.get_param("D_D_2"))

    print("Reading flow (D_A_1_7)...")
    print(await client.get_param("D_A_1_7"))

    print("Reading exchanger info (requires code=005)...")
    print(await client.get_param("D_A_1_1", code="005"))

    await client.close()

asyncio.run(main())
