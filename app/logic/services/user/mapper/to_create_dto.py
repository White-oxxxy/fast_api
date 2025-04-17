from dataclasses import dataclass

from domain.entities.user import UserInput
from dto.user.user import UserCreate
from dto.user.user_response import User
from utils.consts.roles import Roles


@dataclass
class UserDtoToUserCreate:
    @staticmethod
    def execute(user_dto: User) -> UserCreate:
        return UserCreate(
            username=user_dto.username,
            password=user_dto.password,
            email=user_dto.email,
            birthday_date=user_dto.birthday,
            role_id=Roles.to_id(user_dto.role)
        )


@dataclass
class UserInputToUserCreate:
    @staticmethod
    def execute(user: UserInput) -> UserCreate:
        return UserCreate(
            username=user.username,
            password=user.password,
            email=user.email,
            birthday_date=user.birthday,
            role_id=Roles.to_id(user.role)
        )