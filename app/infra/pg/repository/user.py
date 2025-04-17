from sqlalchemy import Select, select
from uuid import UUID

from dto.user.user import UserCreate
from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM


class UserRepositoryORM(BaseRepositoryORM):
    async def get_by_oid(self, required_oid: UUID) -> UserORM | None:
        user: UserORM | None = await self.session.get(UserORM, required_oid)
        return user

    async def create(self, user: UserCreate) -> UserORM:
        user = UserORM(**user.model_dump())
        self.session.add(user)
        return user

    async def get_by_username(self, username: str) -> UserORM | None:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(
            UserORM.username == username
        )
        user: UserORM | None = await self.session.scalar(stmt)
        if not user:
            return None
        return user
