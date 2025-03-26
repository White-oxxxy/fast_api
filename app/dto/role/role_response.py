from dataclasses import dataclass
from pydantic import BaseModel
from typing import Optional


@dataclass
class Role(BaseModel):
    name: str
    description: Optional[str] = None
