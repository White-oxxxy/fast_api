from sqlalchemy import (
    Select,
    select,
)
from uuid import UUID

from domain.entities.user import (
    UserInput,
    User,
)
from domain.repositories.user import IUserRepositoryORM
from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM
from infra.pg.mappers.user import *


class UserRepositoryORM(BaseRepositoryORM, IUserRepositoryORM):
    async def get_by_oid(self, required_oid: UUID) -> User | None:
        user_orm: UserORM | None = await self.session.get(UserORM, required_oid)
        if not user_orm:
            return None

        user_entity: User = GetUserFromORM.execute(user=user_orm)
        return user_entity

    async def create(self, user: UserInput) -> User:
        user_orm: UserORM = UserInputToUserORM.execute(user=user)
        self.session.add(user)
        user_entity: User = GetUserFromORM.execute(user=user_orm)
        return user_entity

    async def get_by_username(self, username: str) -> User | None:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(
            UserORM.username == username
        )
        user_orm: UserORM | None = await self.session.scalar(stmt)
        if not user_orm:
            return None

        user_entity: User = GetUserFromORM.execute(user=user_orm)
        return user_entity
