from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
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
from .options_flow import GruenbeckOptionsFlowHandler

_LOGGER = logging.getLogger(__name__)


async def _validate_host(hass: HomeAssistant, host: str) -> bool:
    """Validate that we can connect to the device."""
    session = async_get_clientsession(hass)
    client = await GruenbeckMC.create(host, session)

    if not client.connected:
        raise Exception("Cannot connect")

    return True


class GruenbeckConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the initial setup flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
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
                # Store everything in options so it can be changed later
                return self.async_create_entry(
                    title=name,
                    data={},  # keep empty so all values remain editable
                    options={
                        CONF_NAME: name,
                        CONF_HOST: host,
                        CONF_SCAN_INTERVAL: scan,
                    },
                )

        data_schema = vol.Schema(
            {
                vol.Required(CONF_NAME): str,
                vol.Required(CONF_HOST): str,
                vol.Optional(
                    CONF_SCAN_INTERVAL,
                    default=DEFAULT_SCAN_INTERVAL,
                ): vol.All(vol.Coerce(int), vol.Range(min=1)),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return GruenbeckOptionsFlowHandler(config_entry)
