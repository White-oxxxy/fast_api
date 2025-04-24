from domain.entities.user import User
from domain.values.user import (
    Username,
    RoleName,
)
from infra.pg.models.user import UserORM
from utils.consts.roles import Roles


class GetUserFromORM:
    @staticmethod
    def execute(user: UserORM) -> User:
        return User(
            oid=user.oid,
            username=Username(user.username),
            role_name=RoleName(Roles.from_id(user.role_id)),
        )