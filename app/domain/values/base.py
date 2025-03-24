from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Any, Generic


VT = TypeVar("VT", bound=Any)

@dataclass(frozen=True)
class BaseValueObject(ABC):
    value: VT

    def __post_init__(self):
        return self.validate()

    @abstractmethod
    def validate(self):
        ...

    @abstractmethod
    def as_generic_type(self) -> VT:
        ...