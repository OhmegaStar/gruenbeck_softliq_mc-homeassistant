from __future__ import annotations
from datetime import datetime
import logging

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .gruenbeck_mc import GruenbeckMC
from .parameter_map import PARAMETERS

_LOGGER = logging.getLogger(__name__)

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

    entities.append(GruenbeckConnectionSuccessRateSensor(client=client, entry_id=entry.entry_id))

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
        return self._state

    async def async_update(self) -> None:
        """Fetch the latest value from the Grünbeck MC device."""
        code = self._meta.get("code")
        resp = await self._client.get_param(self._param, code=code)
        _LOGGER.debug(
            "%s = %r (%s)",
            self._param,
            resp,
            type(resp),
        )
        # `get_param` may return a scalar (int/float/str) when it can
        # directly return the processed value for the requested parameter.
        # It may also return a dict containing a `data` mapping or other
        # raw response shapes. Handle scalars first to avoid AttributeError.
        if isinstance(resp, (int, float, str, datetime)):
            self._state = resp
            return

        # If we got a dict-like response, prefer the `data` mapping if present.
        if isinstance(resp, dict):
            data = resp.get("data") if isinstance(resp.get("data"), dict) else resp

            # Normal case: parameter is present in mapping
            if isinstance(data, dict) and self._param in data:
                self._state = data[self._param]
                return

            # Fallback: if only one key besides "code"
            if isinstance(data, dict):
                keys = [k for k in data.keys() if k != "code"]
                if len(keys) == 1:
                    self._state = data[keys[0]]
                    return

        # Anything else: clear state so Home Assistant shows unavailable
        self._state = None


class GruenbeckConnectionSuccessRateSensor(SensorEntity):
    """Sensor for the connection success rate to the Grünbeck MC device."""

    _attr_should_poll = True
    _attr_native_unit_of_measurement = "%"
   # _attr_device_class = SensorDeviceClass.PERCENT
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, client: GruenbeckMC, entry_id: str):
        self._client = client
        self._attr_unique_id = f"{entry_id}_connection_success_rate"
        self._attr_name = "Grünbeck Connection Success Rate"
        self._state = None

    @property
    def native_value(self):
        return self._state

    async def async_update(self) -> None:
        self._state = self._client.connection_success_rate
