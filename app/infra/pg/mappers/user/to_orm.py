from domain.entities.user import UserInput
from domain.values.user import Username, Password, Email
from infra.pg.models.user import UserORM


class UserInputToUserORM:
    @staticmethod
    def execute(user: UserInput) -> UserORM:
        return UserORM(
            username=Username(user.username).as_generic_type(),
            password=Password(user.password).as_generic_type(),
            email=Email(user.email).as_generic_type(),
            birthday=user.birthday,
            role_id=user.role_id
        )