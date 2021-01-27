from meta_definitions.area import live_calculated_metrics as area_live_calculated_metas
from meta_definitions.area import metrics as area_metrics
from meta_definitions.device import complex_metrics as complex_device_metrics
from meta_definitions.device import live_calculated_metrics as device_live_calculated_metas
from meta_definitions.device import metrics as device_metrics
from meta_definitions.device import temporary_metrics as device_temporary_metas
from meta_definitions.device.definitions import ALL as DEVICE_DEFINITIONS

__all__ = [
    "AREA_METAS",
    "AREA_METRICS_LIVE_CALCULATED",
    "DEVICE_METAS",
    "DEVICE_METAS_TEMPORARY",
    "DEVICE_METRICS_COMPLEX",
    "DEVICE_METRICS_LIVE_CALCULATED",
]


def get_all_metrics_from_file(metrics_file):
    return [
        getattr(metrics_file, meta_variable)
        for meta_variable in dir(metrics_file)
        if meta_variable.startswith("META_") or meta_variable.startswith("METRIC_")
    ]


AREA_METAS = get_all_metrics_from_file(area_metrics)

AREA_METRICS_LIVE_CALCULATED = get_all_metrics_from_file(area_live_calculated_metas)

DEVICE_METAS = get_all_metrics_from_file(device_metrics)

DEVICE_METAS_TEMPORARY = device_temporary_metas.METAS

DEVICE_METRICS_COMPLEX = get_all_metrics_from_file(complex_device_metrics)

DEVICE_METRICS_LIVE_CALCULATED = get_all_metrics_from_file(device_live_calculated_metas)
