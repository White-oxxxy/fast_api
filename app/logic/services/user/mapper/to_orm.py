from dataclasses import dataclass

from dto.user.user import UserCreate
from infra.pg.models.user import UserORM

@dataclass
class CreateUserToORM:
    @staticmethod
    def execute(user: UserCreate) -> UserORM:
        return UserORM(
            username=user.username,
            password=user.password,
            email=user.email,
            role_id=user.role_id,
            birthday=user.birthday_date,
        )