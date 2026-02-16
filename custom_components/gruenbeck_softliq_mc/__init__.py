from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_HOST, CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
from .gruenbeck_mc import GruenbeckMC
from .coordinator import GruenbeckCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "switch"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    host = entry.data[CONF_HOST]
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    client = GruenbeckMC(host)
    coordinator = GruenbeckCoordinator(
        hass,
        client,
        timedelta(seconds=scan_interval),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "client": client,
        "coordinator": coordinator,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    data = hass.data[DOMAIN].pop(entry.entry_id, None)
    if data:
        await data["client"].close()

    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
