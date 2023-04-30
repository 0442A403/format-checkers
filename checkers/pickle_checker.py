import _pickle
import pickle

from checkers.checker import Checker


class PickleChecker(Checker):
    need_schema = False

    def validate_data(self, data: bytes) -> bool:
        try:
            pickle.loads(data)
            return True
        except _pickle.UnpicklingError as e:
            print(e)
            return False
