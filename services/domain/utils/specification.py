# Standard Library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Specification(ABC, Generic[T]):
    @abstractmethod
    def is_satisfied_by(self, candidate: T) -> bool:
        pass

    def __and__(self, other: "Specification[T]") -> "Specification[T]":
        return AndSpecification(self, other)

    def __or__(self, other: "Specification[T]") -> "Specification[T]":
        return OrSpecification(self, other)

    def __invert__(self) -> "Specification[T]":
        return NotSpecification(self)


class AndSpecification(Specification[T]):
    def __init__(self, *specifications: Specification[T]):
        self.specifications = specifications

    def is_satisfied_by(self, candidate: T) -> bool:
        return all(spec.is_satisfied_by(candidate) for spec in self.specifications)


class OrSpecification(Specification[T]):
    def __init__(self, *specifications: Specification[T]):
        self.specifications = specifications

    def is_satisfied_by(self, candidate: T) -> bool:
        return any(spec.is_satisfied_by(candidate) for spec in self.specifications)


class NotSpecification(Specification[T]):
    def __init__(self, specification: Specification[T]):
        self.specification = specification

    def is_satisfied_by(self, candidate: T) -> bool:
        return not self.specification.is_satisfied_by(candidate)
