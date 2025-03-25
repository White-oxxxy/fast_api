from dataclasses import dataclass

from domain.events.base import BaseEvent


@dataclass
class NewRoleCreatedEvent(BaseEvent):
    role_oid: str
    role_name: str
    role_description: str


@dataclass
class GetRoleByOidEvent(BaseEvent):
    role_oid: str


@dataclass
class GetRoleByNameEvent(BaseEvent):
    role_name: str


@dataclass
class RoleFetchedEvent(BaseEvent):
    role_oid: str
    role_name: str
    role_description: str
