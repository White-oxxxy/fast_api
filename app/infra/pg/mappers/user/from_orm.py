from domain.entities.user import User
from domain.values.user import (
    Username,
    RoleName,
    Password,
    Email,
)
from infra.pg.models.user import UserORM


class GetUserFromORM:
    @staticmethod
    def execute(user: UserORM) -> User:
        return User(
            oid=user.oid,
            username=Username(user.username),
            hashed_password=Password(user.password),
            email=Email(user.email),
            birthday=user.birthday,
            role_name=RoleName(user.role.pk),
        )