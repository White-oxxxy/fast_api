from dataclasses import dataclass, field
from pydantic import BaseModel


@dataclass
class Tag(BaseModel):
    name: str
    uploader_name: str

@dataclass
class Text(BaseModel):
    value: str
    uploader_name: str
    tags: list[Tag] = field(default_factory=list)