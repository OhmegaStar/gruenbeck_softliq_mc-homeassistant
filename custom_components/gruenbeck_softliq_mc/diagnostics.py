from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
):
    """Return diagnostics for a config entry."""
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]
    client = data["client"]

    # Latest coordinator data
    device_data = coordinator.data if coordinator.data else {}

    return {
        "entry": {
            "title": entry.title,
            "data": entry.data,
            "options": entry.options,
        },
        "device_data": device_data,
        "host": client.host,
    }
