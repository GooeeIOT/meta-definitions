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
    "phase3_voltage",  # to be renamed to phase_3_voltage
    "volumetric_flow",  # to be renamed to supply_air_volume
)
