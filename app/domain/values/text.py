from dataclasses import dataclass
import re

from .base import BaseValueObject, VT
from domain.exeptions.application.text import (
    EmptyTagNameException,
    EmptyTextValueException,
    IncorrectTagFormatException,
    TagTooLongException,
)


TAG_REGEX = re.compile(r"^#[\w_-]+$")


@dataclass(frozen=True)
class TagName(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyTagNameException()

        if len(self.value) > 15:
            raise TagTooLongException()

        if not self.__is_valid_format(self.value):
            raise IncorrectTagFormatException()

    def as_generic_type(self) -> VT:
        return str(self.value)

    @staticmethod
    def __is_valid_format(tag: str) -> bool:
        return bool(TAG_REGEX.fullmatch(tag))


@dataclass(frozen=True)
class TextValue(BaseValueObject[str]):
    def validate(self):
        if not self.value:
            raise EmptyTextValueException()

    def as_generic_type(self) -> VT:
        return str(self.value)