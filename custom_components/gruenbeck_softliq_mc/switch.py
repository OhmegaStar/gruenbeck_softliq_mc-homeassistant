from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .gruenbeck_mc import GruenbeckMC
from .parameter_map import PARAMETERS


WRITEABLE_SWITCHES = {
    "D_C_5_1": "Operating mode",
    "D_C_8_1": "LED ring behavior",
    "D_C_8_2": "LED blink on salt warning",
    "D_Y_8_10": "Send test email",
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
    ):
    data = hass.data[DOMAIN][entry.entry_id]
    client: GruenbeckMC = data["client"]

    entities = []

    for param, name in WRITEABLE_SWITCHES.items():
        meta = PARAMETERS.get(param)
        if meta:
            entities.append(GruenbeckMCSwitch(client, entry.entry_id, param, meta))

    async_add_entities(entities)


class GruenbeckMCSwitch(SwitchEntity):
    """Switch for writable Grünbeck parameters."""

    def __init__(self, client: GruenbeckMC, entry_id: str, param: str, meta: dict):
        self._client = client
        self._param = param
        self._meta = meta
        self._attr_unique_id = f"{entry_id}_{param}_switch"
        self._attr_name = meta["name"]
        self._state = False

    @property
    def is_on(self):
        return bool(self._state)

    async def async_turn_on(self, **kwargs):
        await self._client.set_param(self._param, "1")
        self._state = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        await self._client.set_param(self._param, "0")
        self._state = False
        self.async_write_ha_state()

    async def async_update(self):
        resp = await self._client.get_param(self._param)

        # Handle scalar responses (value returned directly)
        if isinstance(resp, (int, float, str)):
            val = resp
        elif isinstance(resp, dict):
            data = resp.get("data", {})
            # If param present in mapping
            if self._param in data:
                val = data[self._param]
            else:
                # Fallback: if only one key besides "code"
                keys = [k for k in data.keys() if k != "code"]
                val = data[keys[0]] if len(keys) == 1 else None
        else:
            val = None

        if val is None:
            return

        self._state = str(val) in ("1", "true", "True")