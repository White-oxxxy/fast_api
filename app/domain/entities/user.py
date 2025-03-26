from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.values.user import Password, Username, BirthdayDate


@dataclass(eq=False)
class User(BaseEntity):
    username: Username
    password: Password
    BirthdayDate: BirthdayDate
