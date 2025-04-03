from domain.entities.user import User
from infra.pg.models.user import UserORM
from utils.roles.roles import Roles


class GetUserFromORM:
    @staticmethod
    def execute(user: UserORM) -> User:
        user_entity = User(
            oid=user.oid,
            username=user.username,
            password=user.password,
            role_name=Roles(user.role_id).value,
            birthday=user.birthday
        )
        return user_entity