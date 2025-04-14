from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Tag(BaseModel):
    name: str
    uploader_name: str

class Text(BaseModel):
    value: str
    uploader_name: str