from dataclasses import dataclass
from pydantic import BaseModel
from datetime import datetime

from mixins import IntPkMixin, TimeMixin


@dataclass
class MessageCreate(BaseModel):
    content: "ActionCreate"


@dataclass
class ActionCreate(BaseModel):
    content: str
    uploader_name: str
    upload_time: datetime


@dataclass
class MessageFromDB(MessageCreate, IntPkMixin, TimeMixin): ...


@dataclass
class ActionFromDB(ActionCreate, IntPkMixin, TimeMixin): ...