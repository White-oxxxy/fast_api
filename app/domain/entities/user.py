from dataclasses import dataclass

from datetime import datetime

from domain.entities.base import BaseEntity
from domain.values.user import (
    Username,
    Password,
    Email,
    RoleName
)


@dataclass(eq=False)
class User(BaseEntity):
    username: Username
    role_name: RoleName


@dataclass
class UserInput(BaseEntity):
    username: Username
    password: Password
    email: Email
    birthday: datetime
    role_id: int