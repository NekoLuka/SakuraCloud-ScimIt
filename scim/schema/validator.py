import jsonschema as js


class Validator:
    DEFAULT_SCHEMAS = (  # Supported schema types
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:core:2.0:Group",
        # "urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig",
        # "urn:ietf:params:scim:schemas:core:2.0:ResourceType",
        "urn:ietf:params:scim:schemas:core:2.0:Schema"
    )

    def __init__(self, schemas: list[dict], jsonschema: dict):
        self.schemas = schemas
        self.schema_count = len(schemas)
        self.jsonschema = jsonschema

    def validate_schema(self, schema_index: int) -> bool:
        # TODO: update the error handling
        schema = self.schemas[schema_index]
        return js.validate(instance=schema, schema=self.jsonschema)

    def enforce_schema(self, scim_request: dict) -> bool:
        pass
