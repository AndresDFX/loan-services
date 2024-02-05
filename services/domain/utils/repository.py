# Standard Library
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get_by_external_id(self, external_id: str) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, external_id: str) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        pass
