from httpx import delete
from sqlalchemy import Select, select, delete
from uuid import UUID

from dto.token.token import RefreshTokenCreate
from .base import BaseRepositoryORM
from infra.pg.models.user import RefreshTokenORM


class RefreshTokenRepositoryORM(BaseRepositoryORM):
    async def get_by_oid(self, required_oid: UUID) -> RefreshTokenORM | None:
        token: RefreshTokenORM | None = await self.session.get(RefreshTokenORM, required_oid)
        if not token:
            return None

        return token

    async def create(self, token: RefreshTokenCreate) -> RefreshTokenORM:
        token = RefreshTokenORM(**token.model_dump())
        self.session.add(token)
        return token

    async def get_by_token(self, token: str) -> RefreshTokenORM | None:
        stmt: Select[tuple[RefreshTokenORM]] = select(RefreshTokenORM).where(RefreshTokenORM.token == token)
        token: RefreshTokenORM | None = await self.session.scalar(stmt)
        if not token:
            return None

        return token

    async def delete(self, required_oid: UUID) -> RefreshTokenORM | None:
        stmt = (
            delete(RefreshTokenORM)
            .where(RefreshTokenORM.oid == required_oid)
            .returning(RefreshTokenORM)
        )
        token: RefreshTokenORM | None = await self.session.scalar(stmt)
        if not token:
            return None

        return token