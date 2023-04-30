import msgpack

from checkers.checker import Checker


class MessagePackChecker(Checker):
    need_schema = False

    def validate_data(self, data: bytes) -> bool:
        try:
            msgpack.unpackb(data)
            return True
        except msgpack.FormatError:
            return False
