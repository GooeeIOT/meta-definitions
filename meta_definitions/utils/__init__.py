import json
import os


def write_json_definitions(path, definitions):
    """
    Helper function to create JSON files for the validation of the `value` field
    of the meta definitions.
    """
    if not os.path.isdir(path):
        raise Exception(f"Path doesnt exist: {path}")

    for name in definitions:
        schema = definitions[name]
        if "json_schema" not in schema or "type" not in schema["json_schema"]:
            continue

        with open(f'{path.rstrip("/")}/{name}.json', "w") as fw:
            json_schema_template = {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "description": "Validation for values of dim meta.",
                "type": "object",
                "additionalProperties": True,
                "properties": {"value": {"title": "Value",}},
                "required": ["value"],
            }
            value_schema = schema["json_schema"]
            json_schema_template["properties"]["value"].update(value_schema)
            json.dump(json_schema_template, fw, indent=4)
