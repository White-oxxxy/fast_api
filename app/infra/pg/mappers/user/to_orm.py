from dataclasses import dataclass

from uuid import UUID

from domain.entities.user import User
from domain.values.user import Username, Password, Email
from infra.pg.models.user import UserORM


@dataclass
class UserToUserORM:
    @staticmethod
    def execute(user: User, role_oid: UUID) -> UserORM:
        return UserORM(
            username=Username(user.username).as_generic_type(),
            password=Password(user.hashed_password).as_generic_type(),
            email=Email(user.email).as_generic_type(),
            birthday=user.birthday,
            role_oid=role_oid
        )