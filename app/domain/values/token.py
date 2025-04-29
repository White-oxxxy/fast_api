from dataclasses import dataclass
from re import compile

from domain.exeptions.application.token import (
    EmptyIpAddressException,
    EmptyTokenException,
    IncorrectIpAddressException,
    EmptyUserAgentException,
)
from .base import BaseValueObject, VT


IPV4_REGEX = compile(
    r'^('
    r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.'
    r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.'
    r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.'
    r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'
    r')$'
)

IPV6_REGEX = compile(
    r'^('
    r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
    r'|::([0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}'
    r'|([0-9a-fA-F]{1,4}:){1,6}:'
    r')$'
)


@dataclass(frozen=True)
class TokenName(BaseValueObject):
    def validate(self):
        if not self.value:
            raise EmptyTokenException()

    def as_generic_type(self) -> VT:
        return self.value


@dataclass(frozen=True)
class IpAddress(BaseValueObject):
    def validate(self):
        if not self.value:
            raise EmptyIpAddressException()

        if not self.__is_valid_format(ip=self.value):
            raise IncorrectIpAddressException()

    def as_generic_type(self) -> VT:
        return self.value

    @staticmethod
    def __is_valid_format(ip: str) -> bool:
        return IPV4_REGEX.match(ip) is not None or IPV6_REGEX.match(ip) is not None


@dataclass(frozen=True)
class UserAgent(BaseValueObject):
    def validate(self):
        if not self.value:
            raise EmptyUserAgentException()

    def as_generic_type(self) -> VT:
        return self.value