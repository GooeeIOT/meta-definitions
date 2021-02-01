import json
import os


def write_json_definitions(path, definitions):
    if not os.path.isdir(path):
        raise Exception(f"Path doesnt exist: {path}")

    for name in definitions:
        schema = definitions[name]
        with open(f'{path.rstrip("/")}/{name}.json', "w") as fw:
            json.dump(schema, fw, indent=4)
