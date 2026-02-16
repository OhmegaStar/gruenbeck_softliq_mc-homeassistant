from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN, CONF_HOST, CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL


async def _validate_host(hass: HomeAssistant, host: str) -> None:
    # Her kan du evt. lave et hurtigt kald til /mux_http for at validere
    # For nu antager vi bare at host er gyldig.
    return


class GruenbeckConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        errors = {}

        if user_input is not None:
            host = user_input[CONF_HOST]

            try:
                await _validate_host(self.hass, host)
            except Exception:
                errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title=f"Grünbeck softliQ ({host})",
                    data={CONF_HOST: host},
                    options={CONF_SCAN_INTERVAL: user_input[CONF_SCAN_INTERVAL]},
                )

        data_schema = vol.Schema(
            {
                vol.Required(CONF_HOST): str,
                vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    async def async_step_import(self, user_input) -> FlowResult:
        # Ikke brugt, men kan udbygges hvis du vil understøtte YAML-import
        return await self.async_step_user(user_input)
