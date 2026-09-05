from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import GruenbeckCoordinator
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
    coordinator: GruenbeckCoordinator = data["coordinator"]

    entities = []

    for param, name in WRITEABLE_SWITCHES.items():
        meta = PARAMETERS.get(param)
        if meta:
            entities.append(GruenbeckMCSwitch(coordinator, entry.entry_id, param, meta))

    async_add_entities(entities)


class GruenbeckMCSwitch(CoordinatorEntity, SwitchEntity):
    """Switch for writable Grünbeck parameters."""

    def __init__(self, coordinator: GruenbeckCoordinator, entry_id: str, param: str, meta: dict):
        super().__init__(coordinator)
        self._param = param
        self._meta = meta
        self._attr_unique_id = f"{entry_id}_{param}_switch"
        self._attr_name = meta["name"]

    @property
    def is_on(self):
        value = self.coordinator.data.get(self._param)
        return str(value) in ("1", "true", "True")

    async def async_turn_on(self, **kwargs):
        await self.coordinator.client.set_param(self._param, "1")
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        await self.coordinator.client.set_param(self._param, "0")
        await self.coordinator.async_request_refresh()