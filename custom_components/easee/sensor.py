"""
Support for Easee charger
Author: Niklas Fondberg<niklas.fondberg@gmail.com>
"""
import asyncio
from datetime import timedelta
import logging

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import ATTR_ATTRIBUTION, CONF_NAME, TIME_MINUTES
from homeassistant.exceptions import PlatformNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from .easee.session import EaseeSession, Chargers, Charger, ChargerConfig, ChargerState

DOMAIN = "easee"

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=60)



PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {vol.Required(CONF_USERNAME): cv.string, vol.Required(CONF_PASSWORD): cv.string}
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Easee sensor."""
    timeout = 30

    session = async_get_clientsession(hass)

    sensors = []
    for next_departure in config.get(CONF_NEXT_DEPARTURE):
        sensors.append(
            RMVDepartureSensor(
                session,
                next_departure[CONF_STATION],
                next_departure.get(CONF_DESTINATIONS),
                next_departure.get(CONF_DIRECTION),
                next_departure.get(CONF_LINES),
                next_departure.get(CONF_PRODUCTS),
                next_departure.get(CONF_TIME_OFFSET),
                next_departure.get(CONF_MAX_JOURNEYS),
                next_departure.get(CONF_NAME),
                timeout,
            )
        )

    tasks = [sensor.async_update() for sensor in sensors]
    if tasks:
        await asyncio.wait(tasks)
    if not all(sensor.data.departures for sensor in sensors):
        raise PlatformNotReady

    async_add_entities(sensors)


class ChargersSensor(Entity):
    """Implementation of an RMV departure sensor."""

    def __init__(
        self, session, timeout,
    ):
        """Initialize the sensor."""
        self.session = session
        self.timeout = timeout
        self.chargers[]

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def available(self):
        """Return True if entity is available."""
        return self._state is not None

    @property
    def state(self):
        """Return the next departure time."""
        return self._state

    @property
    def state_attributes(self):
        """Return the state attributes."""
        try:
            return {
                "chargers": "foo",
                "chargers": "bar",
            }
        except IndexError:
            return {}

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return "mdi:flash"

    async def async_update(self):
        """Get the latest data and update the state."""
        return


