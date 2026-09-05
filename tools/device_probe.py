"""Probe the raw Grünbeck Webserver API during development.

Examples:
    python tools/device_probe.py --host 192.168.0.195
    python tools/device_probe.py --params D_Y_6 D_Y_7 D_C_1_1
    python tools/device_probe.py --scan

This is a device probe, not a Home Assistant unit test. Automated smoke tests
for the production client are in ``smoke_test_client.py`` and
``smoke_test_api_modes.py``.
"""

from __future__ import annotations

import argparse
import asyncio
import time
from collections.abc import Iterable

import aiohttp
import xmltodict


DEFAULT_SETS = {
    "basic_info": ("D_Y_6", "D_Y_7", "D_C_1_1"),
    "current_values": ("D_A_1_7", "D_A_1_8", "D_A_1_9"),
    "device_status": ("D_D_1", "D_D_2", "D_D_3"),
    "water_usage": ("D_A_2_1", "D_A_2_2", "D_A_2_3"),
}


def generate_scan_params() -> list[str]:
    groups = {
        "D_A": ((1, 1, 20), (2, 1, 20), (3, 1, 20)),
        "D_D": ((1, 1, 20),),
        "D_C": ((1, 1, 20),),
        "D_Y": ((1, 1, 20),),
        "P_A": ((1, 1, 20),),
        "P_C": ((1, 1, 20),),
        "P_D": ((1, 1, 20),),
        "P_Y": ((1, 1, 20),),
    }
    return [
        f"{prefix}_{group}_{index}"
        for prefix, ranges in groups.items()
        for group, start, end in ranges
        for index in range(start, end + 1)
    ]


async def fetch_show(
    session: aiohttp.ClientSession,
    host: str,
    params: Iterable[str],
) -> tuple[int | None, str, float | None]:
    show = "|".join(params) + "~"
    payload = {"id": "1234", "show": show}
    start = time.perf_counter()
    try:
        async with session.post(
            f"http://{host}/mux_http",
            data=payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=aiohttp.ClientTimeout(total=10),
        ) as response:
            return response.status, await response.text(), time.perf_counter() - start
    except (aiohttp.ClientError, asyncio.TimeoutError) as err:
        return None, f"ERROR: {err}", None


async def probe_set(
    session: aiohttp.ClientSession,
    host: str,
    name: str,
    params: Iterable[str],
) -> None:
    status, text, elapsed = await fetch_show(session, host, params)
    print(f"\n=== {name} ===")
    print(f"HTTP status: {status}; elapsed: {elapsed:.3f}s" if elapsed else text)
    if status is None or not text.strip():
        return
    try:
        print(xmltodict.parse(text))
    except Exception as err:
        print(f"XML parse error: {err}\n{text}")


async def scan_params(
    session: aiohttp.ClientSession,
    host: str,
    params: Iterable[str],
) -> None:
    supported: dict[str, object] = {}
    unsupported: dict[str, str] = {}
    for param in params:
        status, text, _ = await fetch_show(session, host, (param,))
        try:
            if status is None:
                raise RuntimeError(text)
            parsed = xmltodict.parse(text)
            supported[param] = parsed.get("data", parsed)
        except Exception as err:
            unsupported[param] = str(err)

    print(f"Supported ({len(supported)}):")
    for param, value in supported.items():
        print(f"{param}: {value}")
    print(f"\nUnsupported ({len(unsupported)}):")
    for param, error in unsupported.items():
        print(f"{param}: {error}")


async def main(args: argparse.Namespace) -> None:
    async with aiohttp.ClientSession() as session:
        if args.scan:
            await scan_params(session, args.host, generate_scan_params())
            return
        if args.params is not None:
            await probe_set(session, args.host, "custom", args.params)
            return
        for name, group in DEFAULT_SETS.items():
            await probe_set(session, args.host, name, group)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="192.168.0.195")
    parser.add_argument("--params", nargs="+")
    parser.add_argument("--scan", action="store_true")
    asyncio.run(main(parser.parse_args()))