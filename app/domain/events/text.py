from dataclasses import dataclass

from domain.events.base import BaseEvent
from domain.entities.text import Tag


@dataclass
class NewTagCreatedEvent(BaseEvent):
    tag_oid: str
    tag_name: str
    user_oid: str


@dataclass
class NewTextCreated(BaseEvent):
    text_oid: str
    text_value: str
    user_oid: str
    tags: set[Tag]


@dataclass
class GetTagByOidEvent(BaseEvent):
    tag_oid: str


@dataclass
class GetTagByNameEvent(BaseEvent):
    tag_name: str


@dataclass
class TagFetchedEvent(BaseEvent):
    tag_oid: str
    tag_name: str
    user_oid: str


@dataclass
class GetTextByOidEvent(BaseEvent):
    text_oid: str


@dataclass
class GetTextByValueEvent(BaseEvent):
    text_value: str


@dataclass
class GetTextByTagEvent(BaseEvent):
    tag_name: str


@dataclass
class TextFetchedEvent(BaseEvent):
    text_oid: str
    text_value: str
    user_oid: str
