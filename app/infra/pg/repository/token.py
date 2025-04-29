from dataclasses import dataclass

from sqlalchemy import (
    Select,
    select,
    delete,
    Result,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from uuid import UUID

from domain.entities.token import RefreshToken
from domain.repositories.token import IRefreshTokenRepositoryORM
from infra.pg.models.user import (
    UserORM,
    RoleORM,
)
from .base import BaseRepositoryORM
from infra.pg.models.user import RefreshTokenORM
from infra.pg.mappers.token.from_orm import GetRefreshTokenFromORM
from infra.pg.mappers.token.to_orm import RefreshTokenToRefreshTokenORM


@dataclass
class RefreshTokenRepositoryORM(BaseRepositoryORM,IRefreshTokenRepositoryORM):
    token_domain_to_orm_mapper: RefreshTokenToRefreshTokenORM
    token_orm_to_domain_mapper: GetRefreshTokenFromORM

    async def get_by_oid(self, required_oid: UUID) -> RefreshToken | None:
        stmt: Select[tuple["RefreshTokenORM"]] = (
            select(RefreshTokenORM)
            .options(
                selectinload(RefreshTokenORM.user),
                selectinload(RefreshTokenORM.role),
            )
            .where(RefreshTokenORM.oid == required_oid)
        )
        result: Result[tuple["RefreshTokenORM"]] = await self.session.execute(stmt)
        token_orm: RefreshTokenORM | None = result.scalars().one_or_none()
        if not token_orm:
            return None

        token_entity: RefreshToken = GetRefreshTokenFromORM.execute(token_orm=token_orm)
        return token_entity

    async def create(self, refresh_token: RefreshToken) -> RefreshToken:
        stmt: Select[tuple["UserORM"]] = (
            select(UserORM)
            .where(UserORM.username == refresh_token.username)
        )
        result: Result[tuple["UserORM"]] = await self.session.execute(stmt)
        user_orm: UserORM = result.scalars().one_or_none()
        if not user_orm:
            raise

        stmt: Select[tuple["RoleORM"]] = (
            select(RoleORM)
            .where(RoleORM.name == refresh_token.role_name)
        )
        result: Result[tuple["RoleORM"]] = await self.session.execute(stmt)
        role_orm: RoleORM = result.scalars().one_or_none()
        if not role_orm:
            raise
        token_orm: RefreshTokenORM = self.token_domain_to_orm_mapper.execute(
            token_entity=refresh_token,
            user_oid=user_orm.oid,
            role_oid=role_orm.oid
        )
        self.session.add(token_orm)
        try:
            await self.session.flush()
        except IntegrityError:
            raise

        token_entity: RefreshToken = self.token_orm_to_domain_mapper.execute(token_orm)

        return token_entity

    async def update(self, refresh_token: RefreshToken) -> RefreshToken: ...

    async def delete(self, refresh_token: RefreshToken) -> None: ...

