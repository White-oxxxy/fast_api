from dto.user import UserCreate
from infra.pg.models.user import UserORM


class CreateUserToORM:
    def execute(self, users_create: list[UserCreate]) -> list[UserORM]:
        result: list[UserORM] = []
        for user in users_create:
            user_orm: UserORM = self._create_user_orm(user)
            result.append(user_orm)
        return result

    @staticmethod
    def _create_user_orm(user: UserCreate) -> UserORM:
        user_orm = UserORM(
            username=user.username,
            password=user.password,
            role_id=user.role_id,
            birthday=user.birthday_date,
        )
        return user_orm
