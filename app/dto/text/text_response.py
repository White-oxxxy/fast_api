from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Text(BaseModel):
    value: str
    uploader_name: str
    tags = set["Tag"]


@dataclass
class Tag(BaseModel):
    name: str
    uploader_name: str
