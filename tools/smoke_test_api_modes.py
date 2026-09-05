"""Live smoke test for single and multi-parameter production API calls.

Run from the repository root in an environment containing Home Assistant:
    python tools/smoke_test_api_modes.py --host 192.168.0.195
"""

from __future__ import annotations

import argparse
import asyncio

from custom_components.gruenbeck_softliq_mc.gruenbeck_mc import GruenbeckMC


async def main(host: str) -> None:
    client = await GruenbeckMC.create(host)
    try:
        single = await client.get_param("D_A_1_7")
        assert single is not None
        print(f"Single parameter: {single}")

        multiple = await client.get_params(["D_A_1_7", "D_A_1_8", "D_A_1_9"])
        assert isinstance(multiple, dict)
        assert set(("D_A_1_7", "D_A_1_8", "D_A_1_9")).issubset(multiple)
        print(f"Multiple parameters: {multiple}")
    finally:
        await client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="192.168.0.195")
    args = parser.parse_args()
    asyncio.run(main(args.host))