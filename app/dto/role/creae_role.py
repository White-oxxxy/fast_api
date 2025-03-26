from dataclasses import dataclass
from pydantic import BaseModel
from typing import Optional


@dataclass
class RoleCreate(BaseModel):
    name: str
    description: Optional[str] = None
