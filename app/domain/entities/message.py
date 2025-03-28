from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel

from domain.entities.base import BaseEntity


@dataclass(eq=False)
class Action(BaseEntity, BaseModel):
    content: str
    uploader_name: str
    content_upload_time: datetime


@dataclass(eq=False)
class Message(BaseEntity, BaseModel):
    content: Action


@dataclass(eq=False)
class Chat(BaseEntity, BaseModel):
    messages: list[Message]