from sqlalchemy.ext.asyncio import AsyncSession

from dataclasses import dataclass
from uuid import UUID

from domain.entities.user import User, UserInput
from domain.services.user import IUserService
from infra.pg.database import Database
from infra.pg.repository.user import UserRepositoryORM
from infra.pg.models.user import UserORM
from logic.mappers.entity.user import GetUserFromORM
from .mapper.to_create_dto import UserInputToUserCreate
from dto.user.user import UserCreate


@dataclass
class UserService(IUserService):
    database: Database

    async def get_by_username(self, user: UserInput) -> User:
        async with self.database.read_only_async_session as session:
            repo: UserRepositoryORM = self.__get_repo(session=session)
            user_create: UserCreate = UserInputToUserCreate.execute(user=user)
            user_orm: UserORM = await repo.get_by_username(username=user_create.username)

            return GetUserFromORM.execute(user=user_orm)

    async def create(self, user: UserInput) -> User:
        async with self.database.async_session as session:
            repo: UserRepositoryORM = self.__get_repo(session=session)
            user_create: UserCreate = UserInputToUserCreate.execute(user=user)
            user_orm: UserORM = await repo.create(user=user_create)
            await repo.commit()

            return GetUserFromORM.execute(user=user_orm)

    async def get_or_create(self, user: UserInput) -> User:
        async with self.database.async_session as session:
            repo: UserRepositoryORM = self.__get_repo(session=session)
            user_create: UserCreate = UserInputToUserCreate.execute(user=user)
            user_orm: UserORM = await repo.get_by_username(username=user_create.username)
            if not user_orm:
                user_orm: UserORM = await repo.create(user=user_create)
                await repo.commit()

            return GetUserFromORM.execute(user=user_orm)

    async def _get_by_oid(self, required_oid: UUID) -> User | None:
        async with self.database.read_only_async_session as session:
            repo: UserRepositoryORM = self.__get_repo(session=session)
            user_orm: UserORM | None = await repo.get_by_oid(required_oid=required_oid)
            if not user_orm:
                return None

            return GetUserFromORM.execute(user=user_orm)

    @staticmethod
    def __get_repo(session: AsyncSession) -> UserRepositoryORM:
        return UserRepositoryORM(session)
