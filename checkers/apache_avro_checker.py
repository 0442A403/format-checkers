from checkers.checker import Checker

import avro
from avro import schema


class ApacheAvroChecker(Checker):
    need_schema = True

    def __init__(self, schema_str: str):
        self.schema = schema.parse(schema_str)

    def validate_data(self, data: bytes) -> bool:
        try:
            self.schema.validate(data)
            return True
        except Exception as e:
            print(e)
            return False
