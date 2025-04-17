from dataclasses import dataclass, field
from pydantic import BaseModel


@dataclass
class TagCreate(BaseModel):
    name: str
    uploader_name: str


@dataclass
class TextCreate(BaseModel):
    value: str
    uploader_name: str
    tags: list[TagCreate] = field(default_factory=list)



