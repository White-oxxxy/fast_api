from dataclasses import dataclass

from domain.events.base import BaseEvent


@dataclass
class NewUserCreatedEvent(BaseEvent):
    user_oid: str
    username: str
    role_oid: str


@dataclass
class GetUserByOidEvent(BaseEvent):
    user_oid: str


@dataclass
class GetUserByUsernameEvent(BaseEvent):
    username: str


@dataclass
class UserFetchedEvent(BaseEvent):
    user_oid: str
    username: str
    role_oid: str
