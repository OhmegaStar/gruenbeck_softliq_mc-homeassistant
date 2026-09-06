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

        # Group scattered map entries so each protected code section is fetched once.
        self.params_by_code: dict[str | None, list[str]] = {}
        for param, metadata in PARAMETERS.items():
            code = metadata.get("code")
            self.params_by_code.setdefault(code, []).append(param)

    async def _async_update_data(self):
        """Fetch all parameters in batches."""
        try:
            data = {}
            for code, params in self.params_by_code.items():
                response = await self.client.get_params(params, code=code)
                if isinstance(response, dict) and "data" in response:
                    response = response["data"]
                if isinstance(response, dict):
                    data.update(response)

            return data

        except Exception as err:
            raise UpdateFailed(f"Error updating Grünbeck data: {err}") from err
