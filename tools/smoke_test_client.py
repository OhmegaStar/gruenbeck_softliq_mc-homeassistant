"""Live smoke test for the production Gruenbeck client.

Run from the repository root in an environment containing Home Assistant:
    python tools/smoke_test_client.py --host 192.168.0.195
"""

from __future__ import annotations

import argparse
import asyncio

from custom_components.gruenbeck_softliq_mc.gruenbeck_mc import GruenbeckMC


async def main(host: str) -> None:
    client = await GruenbeckMC.create(host)
    try:
        software_version = await client.get_param("D_Y_6")
        assert software_version is not None
        print(f"Software version: {software_version}")

        values = await client.get_params(["D_A_1_7", "D_A_1_6"])
        assert isinstance(values, dict)
        assert "D_A_1_7" in values
        assert "D_A_1_6" in values
        print(f"Current values: {values}")
    finally:
        await client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="192.168.0.195")
    args = parser.parse_args()
    asyncio.run(main(args.host))