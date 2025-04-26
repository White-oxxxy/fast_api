from dataclasses import dataclass

from uuid import UUID

from domain.entities.user import User
from domain.repositories.user import IUserRepositoryORM
from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM
from infra.pg.mappers.user import GetUserFromORM, UserToUserORM


@dataclass
class UserRepositoryORM(BaseRepositoryORM, IUserRepositoryORM):
    domain_user_to_orm_mapper: UserToUserORM
    orm_user_to_domain_mapper: GetUserFromORM

    async def get_by_oid(self, required_oid: UUID) -> User | None:
        user_orm: UserORM | None = await self.session.get(UserORM, required_oid)
        if not user_orm:
            return None

        user_entity: User = self.orm_user_to_domain_mapper.execute(user=user_orm)
        return user_entity

    async def create(self, user: User) -> User:
        user_orm: UserORM = self.domain_user_to_orm_mapper.execute(user=user)
        self.session.add(user)
        user_entity: User = self.orm_user_to_domain_mapper.execute(user=user_orm)
        return user_entity

