from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.values.user import Password, Username


@dataclass(eq=False)
class User(BaseEntity):
    username: Username
    password: Password

    def add_user(self):
        ...

    def get_user_oid(self):
        ...

    def get_user_by_name(self):
        ...

    def fetched_user(self):
        ...