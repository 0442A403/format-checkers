import yaml

from checkers.checker import Checker


class YamlChecker(Checker):
    need_schema = False

    def validate_data(self, data: bytes) -> bool:
        try:
            yaml.load(data.decode('UTF-8'), yaml.loader.SafeLoader)
            return True
        except Exception as e:
            print(e)
            return False
