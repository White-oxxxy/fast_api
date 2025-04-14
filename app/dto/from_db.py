from dataclasses import dataclass

from .mixins import UUIDPkMixin, TimeMixin
from .user.user import UserCreate
from .text.text import TextCreate, TagCreate
from .token.token import RefreshTokenCreate


@dataclass
class UserFromDB(UserCreate, UUIDPkMixin, TimeMixin): ...


@dataclass
class TextFromDB(TextCreate, UUIDPkMixin, TimeMixin): ...


@dataclass
class TagFromDB(TagCreate, UUIDPkMixin, TimeMixin): ...


@dataclass
class RefreshTokenFromDB(RefreshTokenCreate, UUIDPkMixin, TimeMixin): ...