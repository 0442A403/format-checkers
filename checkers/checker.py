from abc import abstractmethod

class Checker:
    need_schema = False

    @abstractmethod
    def validate_data(self, data: bytes) -> bool:
        raise NotImplementedError("Not implemented!")