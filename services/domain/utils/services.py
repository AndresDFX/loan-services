# Standard Library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class AbstractService(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity_data: T) -> T:
        """
        Crea una nueva entidad en la base de datos.

        :param entity_data: Datos de la entidad a crear.
        :return: La entidad creada.
        """
        pass
