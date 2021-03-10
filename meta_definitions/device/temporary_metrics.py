# List of device metas to be renamed or deleted in the near future.
METAS = (
    "air_barometric_pressure",  # to be removed completely later on (confirmed)
    "air_co2",  # to be renamed to space_co2
    "air_voc",  # to be renamed to space_tvoc
    "ambient_noise",  # to be renamed to space_sound_level
    "ambient_temperature",  # to be renamed to  space_temperature
    "boiler_temperature",  # to be removed completely (confirmed)
    "calculated_volume_setpoint",  # to be renamed to calc_supply_air_volume_setpoint
    "chiller_flow_temperature",  # to be renamed to flow_temperature
    "chiller_return_temperature",  # to be renamed to return_temperature
    "cooling_valve",  # to be renamed to cooling_output
    "flowtemp_setpoint",  # to be renamed to flow_temperature_setpoint
    "heating_valve",  # to be renamed to heating_output
    "hvac_setpoint",  # to be removed completely later on (pending confirmation)
    "hvac_state",  # to be renamed to device_enable
    "outside_relative_humidity",  # to be renamed to outside_air_humidity
    "phase3_voltage",  # to be renamed to phase_3_voltage
    "primary_gas_meter",  # to be removed completely (confirmed)
    "red_green_blue",  # to be renamed to rgb
    "relative_humidity",  # to be renamed to return_air_humidity (unifying with return_relative_humidity)
    "return_relative_humidity",  # to be renamed to return_air_humidity (unifying with relative_humidity)
    "returntemp_setpoint",  # to be renamed to return_temperature_setpoint
    "secondary_gas_meter",  # to be removed completely (confirmed)
    "supply_relative_humidity",  # to be renamed to supply_air_humidity
    "supplyair_temperature",  # to be renamed to supply_air_temperature
    "supplyfan_speed",  # to be renamed to supply_fan_speed_output
    "supplyfan_speed_setpoint",  # to be renamed to supply_fan_speed_setpoint
    "supplytemperature_setpoint",  # to be renamed to supply_air_temperature_setpoint
    "volumetric_flow",  # to be renamed to supply_air_volume
)

# Legacy Device Meta Names
META_AIR_BAROMETRIC_PRESSURE = "air_barometric_pressure"
META_AIR_CO2 = "air_co2"
META_AIR_VOC = "air_voc"
META_AMBIENT_NOISE = "ambient_noise"
META_AMBIENT_TEMPERATURE = "ambient_temperature"
META_CO2_SETPOINT = "co2_setpoint"
META_COOLING_VALVE = "cooling_valve"
META_ENABLE = "enable"
META_EXTRACT_FAN_PRESSURE_SETPOINT = "extractfan_pressure_setpoint"
META_EXTRACTFAN_SPEED_SETPOINT = "extractfan_speed_setpoint"
META_EXTRACT_TEMPERATURE_SETPOINT = "extracttemperature_setpoint"
META_FAN_MODE = "fan_mode"
META_FLOW_PRESSURE_SETPOINT = "flowpressure_setpoint"
META_FLOW_TEMPERATURE_SET_POINT = "flowtemp_setpoint"
META_HEAT_PUMP_MODE = "heatpump_mode"
META_HEATING_VALVE = "heating_valve"
META_HUMIDITY_SETPOINT = "humidity_setpoint"
META_LOUVERS = "louvers"
META_MODE = "mode"
META_RETURN_SETPOINT = "return_setpoint"
META_SPEED_SETPOINT = "speed_setpoint"
META_SUPPLY_FAN_PRESSURE_SETPOINT = "supplyfan_pressure_setpoint"
META_SUPPLY_TEMPERATURE_SETPOINT = "supplytemperature_setpoint"
META_X1_SETPOINT = "x1_setpoint"
META_X2_SETPOINT = "x2_setpoint"
META_Y1_SETPOINT = "y1_setpoint"
META_Y2_SETPOINT = "y2_setpoint"
