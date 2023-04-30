import json

from checkers.checker import Checker


class JsonChecker(Checker):
    need_schema = False

    def validate_data(self, data: bytes) -> bool:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError as e:
            return False
