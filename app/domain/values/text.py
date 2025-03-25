from dataclasses import dataclass

from domain.values.base import BaseValueObject, VT
from domain.exeptions.text import EmptyTextException


@dataclass(frozen=True)
class TextValue(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextException

    def as_generic_type(self) -> VT:
        return self.value
