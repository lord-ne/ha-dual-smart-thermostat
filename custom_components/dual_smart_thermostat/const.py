"""const."""

from homeassistant.backports.enum import StrEnum
from homeassistant.const import ATTR_ENTITY_ID
import homeassistant.helpers.config_validation as cv

import voluptuous as vol


DEFAULT_TOLERANCE = 0.3
DEFAULT_NAME = "Dual Smart"
DEFAULT_MAX_FLOOR_TEMP = 28.0

CONF_HEATER = "heater"
CONF_SECONDARY_HEATER = "secondary_heater"
CONF_SECONDARY_HEATING_TIMEOUT = "secondary_heater_timeout"
CONF_COOLER = "cooler"
CONF_SENSOR = "target_sensor"
CONF_FLOOR_SENSOR = "floor_sensor"
CONF_MIN_TEMP = "min_temp"
CONF_MAX_TEMP = "max_temp"
CONF_MAX_FLOOR_TEMP = "max_floor_temp"
CONF_MIN_FLOOR_TEMP = "min_floor_temp"
CONF_TARGET_TEMP = "target_temp"
CONF_TARGET_TEMP_HIGH = "target_temp_high"
CONF_TARGET_TEMP_LOW = "target_temp_low"
CONF_AC_MODE = "ac_mode"
CONF_MIN_DUR = "min_cycle_duration"
CONF_COLD_TOLERANCE = "cold_tolerance"
CONF_HOT_TOLERANCE = "hot_tolerance"
CONF_KEEP_ALIVE = "keep_alive"
CONF_INITIAL_HVAC_MODE = "initial_hvac_mode"
CONF_PRECISION = "precision"
CONF_TEMP_STEP = "target_temp_step"
CONF_OPENINGS = "openings"
CONF_HEAT_COOL_MODE = "heat_cool_mode"
ATTR_TIMEOUT = "timeout"
PRESET_ANTI_FREEZE = "Anti Freeze"

TIMED_OPENING_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_ENTITY_ID): cv.entity_id,
        vol.Required(ATTR_TIMEOUT): vol.All(cv.time_period, cv.positive_timedelta),
    }
)


class HVACMode(StrEnum):
    """HVAC mode for climate devices."""

    # All activity disabled / Device is off/standby
    OFF = "off"

    # Heating
    HEAT = "heat"

    # Cooling
    COOL = "cool"

    # The device supports heating/cooling to a range
    HEAT_COOL = "heat_cool"

    # The temperature is set based on a schedule, learned behavior, AI or some
    # other related mechanism. User is not able to adjust the temperature
    AUTO = "auto"

    # Device is in Dry/Humidity mode
    DRY = "dry"

    # Only the fan is on, not fan and another mode like cool
    FAN_ONLY = "fan_only"

    IDLE = "idle"


class HVACAction(StrEnum):
    """HVAC action for climate devices."""

    COOLING = "cooling"
    DRYING = "drying"
    FAN = "fan"
    HEATING = "heating"
    IDLE = "idle"
    OFF = "off"


class ToleranceDevice(StrEnum):
    """Tolerance device for climate devices."""

    HEATER = "heater"
    COOLER = "cooler"
    AUTO = "auto"
