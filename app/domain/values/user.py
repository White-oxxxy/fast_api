from dataclasses import dataclass
from re import fullmatch

from domain.exeptions.user import (
    EmptyUsernameException,
    UsernameTooLongException,
    IncorrectUsernameException,
)
from domain.values.base import BaseValueObject, VT


@dataclass(frozen=True)
class Username(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyUsernameException

        if len(self.value) > 255:
            raise UsernameTooLongException

        if not fullmatch(r"\w+", self.value):
            raise IncorrectUsernameException

    def as_generic_type(self) -> VT:
        return str(self.value)


@dataclass(frozen=True)
class Password(BaseValueObject):
    value: str

    def validate(self): ...

    def as_generic_type(self) -> VT:
        return str(self.value)
