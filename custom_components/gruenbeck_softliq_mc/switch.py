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
        data = resp.get("data", {})
        if self._param in data:
            self._state = data[self._param] in ("1", "true", "True")
