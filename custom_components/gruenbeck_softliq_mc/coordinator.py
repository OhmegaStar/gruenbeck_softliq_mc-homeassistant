from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .gruenbeck_mc import GruenbeckMC
from .parameter_map import PARAMETERS

_LOGGER = logging.getLogger(__name__)


class GruenbeckCoordinator(DataUpdateCoordinator):
    """Coordinator for Grünbeck softliQ MC."""

    def __init__(self, hass: HomeAssistant, client: GruenbeckMC, interval: timedelta):
        super().__init__(
            hass,
            _LOGGER,
            name="gruenbeck_softliq_mc",
            update_interval=interval,
        )
        self.client = client

        # Split parameters into normal and code=005
        self.normal_params = [p for p, m in PARAMETERS.items() if "code" not in m]
        self.code_params = [p for p, m in PARAMETERS.items() if m.get("code") == "005"]

    async def _async_update_data(self):
        """Fetch all parameters in batches."""
        try:
            # Normal parameters
            normal_resp = await self.client.get_params(self.normal_params)

            # Code=005 parameters
            code_resp = await self.client.get_params(self.code_params, code="005")

            data = {}
            if "data" in normal_resp:
                data.update(normal_resp["data"])
            if "data" in code_resp:
                data.update(code_resp["data"])

            return data

        except Exception as err:
            raise UpdateFailed(f"Error updating Grünbeck data: {err}") from err
