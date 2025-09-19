from abc import ABC, abstractmethod


class StorageEngine(ABC):
    @abstractmethod
    def set(self, key: bytes, value: bytes) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: bytes):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError
