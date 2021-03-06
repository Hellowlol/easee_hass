"""Easee Charger constants."""
DOMAIN = "easee"
MEASURED_CONSUMPTION_DAYS = "measured_consumption_days"
VERSION = "0.9.14"
CONF_MONITORED_SITES = "monitored_sites"
CUSTOM_UNITS = "custom_units"
PLATFORMS = ("sensor", "switch")
SCAN_INTERVAL_SECONDS = 60
MEASURED_CONSUMPTION_OPTIONS = {
    "1": "1",
    "7": "7",
    "14": "14",
    "30": "30",
    "365": "365",
}
CUSTOM_UNITS_OPTIONS = {
    "kW": "Power kW to W",
    "kWh": "Energy kWh to Wh",
}
CUSTOM_UNITS_TABLE = {
    "kW": "W",
    "kWh": "Wh",
}
EASEE_ENTITIES = {
    "smartCharging": {
        "type": "switch",
        "key": "state.smartCharging",
        "attrs": [],
        "units": None,
        "convert_units_func": None,
        "icon": "mdi:auto-fix",
        "switch_func": "smart_charging",
    },
    "cableLocked": {
        "type": "switch",
        "key": "state.lockCablePermanently",
        "attrs": ["state.lockCablePermanently", "state.cableLocked",],
        "units": None,
        "convert_units_func": None,
        "icon": "mdi:lock",
        "state_func": lambda state: state["lockCablePermanently"]
        or state["cableLocked"],
        "switch_func": "lockCablePermanently",
    },
    "status": {
        "key": "state.chargerOpMode",
        "attrs": [
            "config.phaseMode",
            "state.outputPhase",
            "state.ledMode",
            "state.cableRating",
            "config.limitToSinglePhaseCharging",
            "config.localNodeType",
            "config.localAuthorizationRequired",
            "config.ledStripBrightness",
            "site.id",
            "site.name",
            "site.siteKey",
            "circuit.id",
            "circuit.ratedCurrent",
        ],
        "units": None,
        "convert_units_func": None,
        "icon": "mdi:ev-station",
    },
    "total_power": {
        "key": "state.totalPower",
        "attrs": [],
        "units": "kW",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:flash",
    },
    "session_energy": {
        "key": "state.sessionEnergy",
        "attrs": [],
        "units": "kWh",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:flash",
    },
    "energy_per_hour": {
        "key": "state.energyPerHour",
        "attrs": [],
        "units": "kWh",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:flash",
    },
    "online": {
        "key": "state.isOnline",
        "attrs": [
            "state.latestPulse",
            "config.wiFiSSID",
            "state.wiFiAPEnabled",
            "state.wiFiRSSI",
            "state.cellRSSI",
            "state.localRSSI",
        ],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:wifi",
    },
    "outputCurrent": {
        "key": "state.outputCurrent",
        "attrs": [],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
    },
    "inCurrent": {
        "key": "state.inCurrentT2",
        "attrs": [
            "state.outputCurrent",
            "state.inCurrentT2",
            "state.inCurrentT3",
            "state.inCurrentT4",
            "state.inCurrentT5",
        ],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
        "state_func": lambda state: float(
            max(
                state["inCurrentT2"],
                state["inCurrentT3"],
                state["inCurrentT4"],
                state["inCurrentT5"],
            )
        ),
    },
    "circuitCurrent": {
        "key": "state.circuitTotalPhaseConductorCurrentL1",
        "attrs": [
            "circuit.id",
            "circuit.circuitPanelId",
            "circuit.panelName",
            "circuit.ratedCurrent",
            "state.circuitTotalAllocatedPhaseConductorCurrentL1",
            "state.circuitTotalAllocatedPhaseConductorCurrentL2",
            "state.circuitTotalAllocatedPhaseConductorCurrentL3",
            "state.circuitTotalPhaseConductorCurrentL1",
            "state.circuitTotalPhaseConductorCurrentL2",
            "state.circuitTotalPhaseConductorCurrentL3",
        ],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
        "state_func": lambda state: float(
            max(
                state["circuitTotalPhaseConductorCurrentL1"]
                if state["circuitTotalPhaseConductorCurrentL1"] is not None
                else 0.0,
                state["circuitTotalPhaseConductorCurrentL2"]
                if state["circuitTotalPhaseConductorCurrentL2"] is not None
                else 0.0,
                state["circuitTotalPhaseConductorCurrentL3"]
                if state["circuitTotalPhaseConductorCurrentL3"] is not None
                else 0.0,
            )
        ),
    },
    "dynamicCircuitCurrent": {
        "key": "state.dynamicCircuitCurrentP1",
        "attrs": [
            "circuit.id",
            "circuit.circuitPanelId",
            "circuit.panelName",
            "circuit.ratedCurrent",
            "state.dynamicCircuitCurrentP1",
            "state.dynamicCircuitCurrentP2",
            "state.dynamicCircuitCurrentP3",
        ],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
        "state_func": lambda state: float(
            max(
                state["dynamicCircuitCurrentP1"],
                state["dynamicCircuitCurrentP2"],
                state["dynamicCircuitCurrentP3"],
            )
        ),
    },
    "maxCircuitCurrent": {
        "key": "config.circuitMaxCurrentP1",
        "attrs": [
            "circuit.id",
            "circuit.circuitPanelId",
            "circuit.panelName",
            "circuit.ratedCurrent",
            "config.circuitMaxCurrentP1",
            "config.circuitMaxCurrentP2",
            "config.circuitMaxCurrentP3",
        ],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
        "state_func": lambda config: float(
            max(
                config["circuitMaxCurrentP1"],
                config["circuitMaxCurrentP2"],
                config["circuitMaxCurrentP3"],
            )
        ),
    },
    "dynamicChargerCurrent": {
        "key": "state.dynamicChargerCurrent",
        "attrs": ["state.dynamicChargerCurrent",],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
    },
    "maxChargerCurrent": {
        "key": "config.maxChargerCurrent",
        "attrs": ["config.maxChargerCurrent",],
        "units": "A",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
    },
    "voltage": {
        "key": "state.voltage",
        "attrs": [
            "state.inVoltageT1T2",
            "state.inVoltageT1T3",
            "state.inVoltageT1T4",
            "state.inVoltageT1T5",
            "state.inVoltageT2T3",
            "state.inVoltageT2T4",
            "state.inVoltageT2T5",
            "state.inVoltageT3T4",
            "state.inVoltageT3T5",
            "state.inVoltageT4T5",
        ],
        "units": "V",
        "convert_units_func": "round_2_dec",
        "icon": "mdi:sine-wave",
    },
    "reasonForNoCurrent": {
        "key": "state.reasonForNoCurrent",
        "attrs": ["state.reasonForNoCurrent", "state.reasonForNoCurrent",],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:alert-circle",
    },
    "isEnabled": {
        "type": "switch",
        "key": "config.isEnabled",
        "attrs": [],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:power-standby",
        "switch_func": "enable_charger",
    },
    "enableIdleCurrent": {
        "type": "switch",
        "key": "config.enableIdleCurrent",
        "attrs": [],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:current-dc",
        "switch_func": "enable_idle_current",
    },
    "update_available": {
        "key": "state.chargerFirmware",
        "attrs": ["state.chargerFirmware", "state.latestFirmware",],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:file-download",
        "state_func": lambda state: int(state["chargerFirmware"])
        < int(state["latestFirmware"]),
    },
    "basic_schedule": {
        "key": "schedule.id",
        "attrs": [
            "schedule.id",
            "schedule.chargeStartTime",
            "schedule.chargeStopTime",
            "schedule.repeat",
        ],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:clock-check",
        "state_func": lambda schedule: True if schedule is not None else False,
    },
    "costPerKWh": {
        "key": "site.costPerKWh",
        "attrs": [
            "site.costPerKWh",
            "site.costPerKwhExcludeVat",
            "site.vat",
            "site.costPerKwhExcludeVat",
            "site.currencyId",
        ],
        "units": "",
        "convert_units_func": None,
        "icon": "mdi:currency-usd",
    },
}
