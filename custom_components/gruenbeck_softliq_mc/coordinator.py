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
        self.code_005_params = [p for p, m in PARAMETERS.items() if m.get("code") == "005"]
        self.code_290_params = [p for p, m in PARAMETERS.items() if m.get("code") == "290"]

    async def _async_update_data(self):
        """Fetch all parameters in batches."""
        try:
            # Normal parameters
            normal_resp = await self.client.get_params(self.normal_params)

            # Code=005 parameters
            code_005_resp = await self.client.get_params(self.code_005_params, code="005")

            # Code=290 parameters
            code_290_resp = await self.client.get_params(self.code_290_params, code="290")

            data = {}
            for response in (normal_resp, code_005_resp, code_290_resp):
                if isinstance(response, dict) and "data" in response:
                    response = response["data"]
                if isinstance(response, dict):
                    data.update(response)

            return data

        except Exception as err:
            raise UpdateFailed(f"Error updating Grünbeck data: {err}") from err
