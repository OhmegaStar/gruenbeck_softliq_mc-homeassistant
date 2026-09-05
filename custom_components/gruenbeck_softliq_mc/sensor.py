from __future__ import annotations

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import GruenbeckCoordinator
from .parameter_map import PARAMETERS

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up all Grünbeck MC sensors."""
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator: GruenbeckCoordinator = data["coordinator"]

    entities: list[SensorEntity] = []

    for param, meta in PARAMETERS.items():
        # Only create sensors for readable parameters
        if meta.get("access") in ("r", "rw"):
            entities.append(
                GruenbeckMCSensor(
                    coordinator=coordinator,
                    entry_id=entry.entry_id,
                    param=param,
                    meta=meta,
                )
            )

    entities.append(
        GruenbeckConnectionSuccessRateSensor(
            coordinator=coordinator,
            entry_id=entry.entry_id,
        )
    )

    async_add_entities(entities)


class GruenbeckMCSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Grünbeck MC sensor."""

    def __init__(
        self,
        coordinator: GruenbeckCoordinator,
        entry_id: str,
        param: str,
        meta: dict,
    ):
        super().__init__(coordinator)
        self._param = param
        self._meta = meta

        self._attr_unique_id = f"{entry_id}_{param}"
        self._attr_name = meta.get("name", param)
        self._attr_native_unit_of_measurement = meta.get("unit")
        self._state = None

        # Device class
        if meta.get("device_class") == "water":
            self._attr_device_class = SensorDeviceClass.WATER
        elif meta.get("device_class") == "timestamp":
            self._attr_device_class = SensorDeviceClass.TIMESTAMP

        # State class
        if meta.get("state_class") == "measurement":
            self._attr_state_class = SensorStateClass.MEASUREMENT
        elif meta.get("state_class") == "total":
            self._attr_state_class = SensorStateClass.TOTAL
        elif meta.get("state_class") == "total_increasing":
            self._attr_state_class = SensorStateClass.TOTAL_INCREASING

    @property
    def native_value(self):
        return self.coordinator.data.get(self._param)


class GruenbeckConnectionSuccessRateSensor(CoordinatorEntity, SensorEntity):
    """Sensor for the connection success rate to the Grünbeck MC device."""

    _attr_native_unit_of_measurement = "%"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator: GruenbeckCoordinator, entry_id: str):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry_id}_connection_success_rate"
        self._attr_name = "Grünbeck Connection Success Rate"

    @property
    def native_value(self):
        return self.coordinator.client.connection_success_rate
