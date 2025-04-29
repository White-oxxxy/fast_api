from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import Select, select, Result
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from domain.entities.user import User
from domain.repositories.user import IUserRepositoryORM
from domain.exeptions.infra.user import (
    UserAlreadyExistedException,
    RoleDoesntCreatedException,
)
from infra.pg.models.user import RoleORM
from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM
from infra.pg.mappers.user import GetUserFromORM, UserToUserORM


@dataclass
class UserRepositoryORM(BaseRepositoryORM, IUserRepositoryORM):
    domain_user_to_orm_mapper: UserToUserORM
    orm_user_to_domain_mapper: GetUserFromORM

    async def get_by_oid(self, required_oid: UUID) -> User | None:
        stmt: Select[tuple["UserORM"]] = (
            select(UserORM)
            .where(UserORM.oid == required_oid)
            .options(selectinload(UserORM.role))
        )
        result: Result[tuple["UserORM"]] = await self.session.execute(stmt)
        user_orm: UserORM | None = result.scalars().one_or_none()
        if not user_orm:
            return None

        user_entity: User = self.orm_user_to_domain_mapper.execute(user=user_orm)
        return user_entity

    async def create(self, user: User) -> User:
        stmt: Select[tuple["RoleORM"]] = select(RoleORM).where(RoleORM.name == user.role_name)
        result: Result[tuple["RoleORM"]] = await self.session.execute(stmt)
        role_orm: RoleORM | None = result.scalar_one_or_none()
        if not role_orm:
            raise RoleDoesntCreatedException

        user_orm: UserORM = self.domain_user_to_orm_mapper.execute(user=user, role_oid=role_orm.oid)
        self.session.add(user_orm)
        try:
            await self.session.flush()
        except IntegrityError:
            raise UserAlreadyExistedException()

        user_entity: User = self.orm_user_to_domain_mapper.execute(user=user_orm)
        return user_entity

