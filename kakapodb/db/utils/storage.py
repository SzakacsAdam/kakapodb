from abc import ABC
from abc import abstractmethod
from typing import List, Optional

from kakapodb.db.document import Document


class BaseStorage(ABC):
    @abstractmethod
    def read(self) -> Optional[List[Document]]:
        raise NotImplementedError

    @abstractmethod
    def write(self, data: List[Document]) -> None:
        raise NotImplementedError


class MemoryStorage(BaseStorage):
    def __init__(self) -> None:
        self.storage: Optional[List[Document]] = None

    def read(self) -> Optional[List[Document]]:
        return self.storage

    def write(self, data: List[Document]) -> None:
        self.storage = data
