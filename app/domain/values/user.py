from dataclasses import dataclass
import re

from .base import BaseValueObject, VT
from domain.exeptions.application.user import (
    EmptyNameException,
    NameTooLongException,
    EmptyPasswordException,
    EmptyEmailException,
    IncorrectEmailFormatException,
    EmptyRoleException,
)


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)


@dataclass(frozen=True)
class Username(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyNameException()

        if len(self.value) > 15:
            raise NameTooLongException()

    def as_generic_type(self) -> VT:
        return str(self.value)


@dataclass(frozen=True)
class Password(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyPasswordException()

    def as_generic_type(self) -> VT:
        return str(self.value)


@dataclass(frozen=True)
class Email(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyEmailException()

        if not self.__is_valid_email(email=self.value):
            raise IncorrectEmailFormatException()

    def as_generic_type(self) -> VT:
        return str(self.value)

    @staticmethod
    def __is_valid_email(email: str) -> bool:
        return bool(EMAIL_REGEX.fullmatch(email))


@dataclass(frozen=True)
class RoleName(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyRoleException

    def as_generic_type(self) -> VT:
        return str(self.value)


