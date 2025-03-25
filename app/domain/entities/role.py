from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.values.role import Name


@dataclass(eq=False)
class Role(BaseEntity):
    name: Name
    description: str

    def add_role(self):
        ...

    def get_role_by_oid(self):
        ...

    def get_role_by_name(self):
        ...

    def fetched_role(self):
        ...
