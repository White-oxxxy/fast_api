from dataclasses import dataclass

from domain.values.base import BaseValueObject, VT
from domain.exeptions.role import EmptyNameException, NameTooLongException


@dataclass(frozen=True)
class Name(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyNameException

        if len(self.value) > 255:
            raise NameTooLongException

    def as_generic_type(self) -> VT:
        return str(self.value)
