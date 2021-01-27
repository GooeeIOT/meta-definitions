from meta_definitions.area import live_calculated_metrics as area_live_calculated_metas
from meta_definitions.area import metrics as area_metrics
from meta_definitions.device import complex_metrics as complex_device_metrics
from meta_definitions.device import live_calculated_metrics as device_live_calculated_metas
from meta_definitions.device import metrics as device_metrics
from meta_definitions.device import temporary_metrics as device_temporary_metas
from meta_definitions.device.definitions import ALL as DEVICE_META_DEFINITIONS

__all__ = [
    "COMPLEX_METRICS_DEVICE",
    "METAS_AREA",
    "METAS_AREA_LIVE_CALCULATED",
    "METAS_DEVICE",
    "METAS_DEVICE_LIVE_CALCULATED",
    "METAS_DEVICE_TEMPORARY",
]


def get_all_metrics_from_file(metrics_file):
    return [
        getattr(metrics_file, meta_variable)
        for meta_variable in dir(metrics_file)
        if meta_variable.startswith("META_") or meta_variable.startswith("METRIC_")
    ]


ALL = DEVICE_META_DEFINITIONS

METAS_AREA = get_all_metrics_from_file(area_metrics)

METAS_AREA_LIVE_CALCULATED = get_all_metrics_from_file(area_live_calculated_metas)

METAS_DEVICE = get_all_metrics_from_file(device_metrics)

METAS_DEVICE_LIVE_CALCULATED = get_all_metrics_from_file(device_live_calculated_metas)

METAS_DEVICE_TEMPORARY = device_temporary_metas.METAS

COMPLEX_METRICS_DEVICE = get_all_metrics_from_file(complex_device_metrics)
