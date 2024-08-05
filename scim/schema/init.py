import json
from ruamel import yaml


class Init:
    ALLOWED_EXTENSIONS = ("yaml", "yml", "json")

    @classmethod
    def init(cls, schema_path: str, jsonschema_path: str):
        extension = schema_path.rsplit(".", 1)[1]
        if extension not in cls.ALLOWED_EXTENSIONS:
            raise ImportError(
                "Incorrect file extension, allowed values are: {}".format(" ".join(cls.ALLOWED_EXTENSIONS))
            )
        with open(schema_path, "r") as schema_reader:
            if extension == "json":
                schemas = json.load(schema_reader)
            else:
                schemas = yaml.load(schema_reader)
        with open(jsonschema_path, "r") as jsonschema_reader:
            jsonschema = json.load(jsonschema_reader)
        return {"schemas": schemas, "jsonschema": jsonschema}
