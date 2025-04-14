from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class TextCreate(BaseModel):
    value: str
    uploader_name: str


@dataclass
class TagCreate(BaseModel):
    name: str
    uploader_name: str

