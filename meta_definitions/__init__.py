# Read the metric names defined in anx_snowflake_sqlalchemy.models.device_metric_names
from meta_definitions.area import life_calculated_metrics as area_life_calculated_metas
from meta_definitions.area import metrics as area_metrics
from meta_definitions.area import temporary_metrics as area_temporary_metas
from meta_definitions.device import life_calculated_metrics as device_life_calculated_metas
from meta_definitions.device import metrics as device_metrics
from meta_definitions.device import temporary_metrics as device_temporary_metas

__all__ = [
    "METAS_AREA",
    "METAS_AREA_LIFE_CALCULATED",
    "METAS_AREA_TEMPORARY",
    "METAS_DEVICE",
    "METAS_DEVICE_LIFE_CALCULATED",
    "METAS_DEVICE_TEMPORARY",
]


def get_all_metrics_from_file(metrics_file):
    return [
        getattr(metrics_file, meta_variable)
        for meta_variable in dir(metrics_file)
        if meta_variable.startswith("META_")
    ]


METAS_AREA = get_all_metrics_from_file(area_metrics)

METAS_AREA_LIFE_CALCULATED = get_all_metrics_from_file(area_life_calculated_metas)

METAS_AREA_TEMPORARY = area_temporary_metas.METAS

METAS_DEVICE = get_all_metrics_from_file(device_metrics)

METAS_DEVICE_LIFE_CALCULATED = get_all_metrics_from_file(device_metrics)

METAS_DEVICE_TEMPORARY = device_temporary_metas.METAS
