from dataclasses import dataclass

from datetime import datetime

from domain.entities.base import BaseEntity
from domain.values.user import (
    Username,
    Password,
    Email,
    RoleName
)


@dataclass
class User(BaseEntity):
    username: Username
    hashed_password: Password
    email: Email
    birthday: datetime
    role_name: RoleName