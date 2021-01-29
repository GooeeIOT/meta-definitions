from meta_definitions.device.definitions import ALL
from meta_definitions.utils import write_json_definitions


def write_json_meta_definitions(path: str):
    """Writes json files of the device definitions in the given directory"""
    return write_json_definitions(path, ALL)
