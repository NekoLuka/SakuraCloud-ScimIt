from scim import schema
from dotenv import load_dotenv

import os


def main():
    load_dotenv()

    schema_validator = schema.Validator(
        # Load and convert the required schema files
        **schema.Init.init(os.environ.get("SCIMIT_SCHEMA"), os.environ.get(
            "SCIMIT_SCIM_JSONSCHEMA", "scim-json-schema.json"
        ))
    )
    for i in range(schema_validator.schema_count):
        valid = schema_validator.validate_schema(i)
        if not valid:
            raise schema.error.SchemaValidationError()
