from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .gruenbeck_mc import GruenbeckMC
from .parameter_map import PARAMETERS


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up all Grünbeck MC sensors."""
    data = hass.data[DOMAIN][entry.entry_id]
    client: GruenbeckMC = data["client"]

    entities: list[SensorEntity] = []

    for param, meta in PARAMETERS.items():
        # Only create sensors for readable parameters
        if meta.get("access") in ("r", "rw"):
            entities.append(
                GruenbeckMCSensor(
                    client=client,
                    entry_id=entry.entry_id,
                    param=param,
                    meta=meta,
                )
            )

    async_add_entities(entities)


class GruenbeckMCSensor(SensorEntity):
    """Representation of a Grünbeck MC sensor."""

    _attr_should_poll = True

    def __init__(self, client: GruenbeckMC, entry_id: str, param: str, meta: dict):
        self._client = client
        self._param = param
        self._meta = meta

        self._attr_unique_id = f"{entry_id}_{param}"
        self._attr_name = meta.get("name", param)
        self._attr_native_unit_of_measurement = meta.get("unit")
        self._state = None

    @property
    def native_value(self):
        return self._state

    async def async_update(self) -> None:
        """Fetch the latest value from the Grünbeck MC device."""
        code = self._meta.get("code")
        resp = await self._client.get_param(self._param, code=code)

        data = resp.get("data", {})

        # Normal case: parameter is present
        if self._param in data:
            self._state = data[self._param]
            return

        # Fallback: if only one key besides "code"
        keys = [k for k in data.keys() if k != "code"]
        if len(keys) == 1:
            self._state = data[keys[0]]
        else:
            self._state = None
