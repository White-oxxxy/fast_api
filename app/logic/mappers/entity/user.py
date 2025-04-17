from domain.entities.user import User
from infra.pg.models.user import UserORM
from utils.consts.roles import Roles


class GetUserFromORM:
    @staticmethod
    def execute(user: UserORM) -> User:
        return User(
            oid=user.oid,
            username=user.username,
            role_name=Roles.from_id(user.role_id),
        )
