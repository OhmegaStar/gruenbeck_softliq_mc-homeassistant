from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_HOST, CONF_NAME

from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    DOMAIN,
    CONF_NAME,
    CONF_HOST,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
)
from .gruenbeck_mc import GruenbeckMC

_LOGGER = logging.getLogger(__name__)


async def _validate_host(hass: HomeAssistant, host: str) -> bool:
    """Validate that we can connect to the device."""
    session = async_get_clientsession(hass)
    client = await GruenbeckMC.create(host, session)

    if not client.connected:
        raise Exception("Cannot connect")

    return True


class GruenbeckOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Grünbeck softliQ MC."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        errors = {}

        if user_input is not None:
            name = user_input[CONF_NAME]
            host = user_input[CONF_HOST]
            scan = user_input[CONF_SCAN_INTERVAL]

            try:
                await _validate_host(self.hass, host)
            except Exception:
                errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title="",
                    data={
                        CONF_NAME: name,
                        CONF_HOST: host,
                        CONF_SCAN_INTERVAL: scan,
                    },
                )

        # Load current values
        current = self.config_entry.options

        data_schema = vol.Schema(
            {
                vol.Required(CONF_NAME, default=current.get(CONF_NAME)): str,
                vol.Required(CONF_HOST, default=current.get(CONF_HOST)): str,
                vol.Required(
                    CONF_SCAN_INTERVAL,
                    default=current.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
                ): int,
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=data_schema,
            errors=errors,
        )
