from dataclasses import dataclass
from pydantic import BaseModel
from typing import Optional

from mixins import IntPkMixin, TimeMixin


@dataclass
class RoleCreate(BaseModel):
    name: str
    uploader_name: str
    description: Optional[str] = None


@dataclass
class RoleFromDB(RoleCreate, IntPkMixin, TimeMixin): ...
