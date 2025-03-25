from dataclasses import dataclass

from domain.values.base import BaseValueObject, VT
from domain.exeptions.tag import (
    EmptyTagNameException,
    TagTooLongException,
    IncorrectTagPrefixException,
)


@dataclass(frozen=True)
class Name(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTagNameException

        if self.value[0] != "#":
            raise IncorrectTagPrefixException

        if len(self.value) > 255:
            raise TagTooLongException

    def as_generic_type(self) -> VT:
        return str(self.value)
