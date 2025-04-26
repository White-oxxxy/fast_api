from domain.entities.user import User
from domain.values.user import Username, Password, Email
from infra.pg.models.user import UserORM
from utils.consts.roles import Roles

class UserToUserORM:
    @staticmethod
    def execute(user: User) -> UserORM:
        return UserORM(
            username=Username(user.username).as_generic_type(),
            password=Password(user.hashed_password).as_generic_type(),
            email=Email(user.email).as_generic_type(),
            birthday=user.birthday,
            role_id=Roles.to_id(name=user.role_name.as_generic_type())
        )