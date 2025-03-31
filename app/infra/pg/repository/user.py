from sqlalchemy import Result, Select, select
from datetime import datetime
from uuid import UUID

from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM, RoleORM
from infra.pg.repository.exceptions.user import EmptyRoleAnswer


class RoleRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> RoleORM | None:
        role: RoleORM | None = await self.session.get(RoleORM, required_id)
        return role

    async def get_by_oid(self, required_oid: UUID) -> RoleORM | None:
        role: RoleORM | None = await self.session.get(RoleORM, required_oid)
        return role

    async def create(self, name: str, description: str) -> RoleORM:
        role = RoleORM(name=name, description=description)
        self.session.add(role)

        return role

    async def get_by_name(self, name: str) -> RoleORM | None:
        stmt: Select[tuple[RoleORM]] = (
            select(RoleORM).where(RoleORM.name == name).limit(1)
        )
        role: RoleORM | None = await self.session.scalar(stmt)
        if not role:
            return None

        return role


class UserRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> UserORM | None:
        user: UserORM | None = await self.session.get(UserORM, required_id)

        return user

    async def get_by_oid(self, required_oid: int) -> UserORM | None:
        user: UserORM | None = await self.session.get(UserORM, required_oid)

        return user

    async def create(self, username: str, password: str, role: str, birthday: datetime) -> UserORM:
        stmt: Select[tuple[RoleORM]] = (
            select(RoleORM).where(RoleORM.name == role).limit(1)
        )
        role: RoleORM | None = await self.session.scalar(stmt)
        if not role:
            raise EmptyRoleAnswer
        user = UserORM(username=username, password=password, role_id=role.pk, birthday=birthday)
        self.session.add(user)

        return user

    async def get_by_username(self, username: str) -> UserORM | None:
        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.username == username)
        user: UserORM | None = await self.session.scalar(stmt)
        if not user:
            return None

        return user

    async def get_by_role(self, role: str) -> list[UserORM]:
        stmt: Select[tuple[RoleORM]] = select(RoleORM).where(RoleORM.name == role)
        role: RoleORM | None = await self.session.scalar(stmt)
        if not role:
            raise EmptyRoleAnswer

        stmt: Select[tuple[UserORM]] = select(UserORM).where(UserORM.role_id == role.pk)
        result: Result = await self.session.execute(stmt)
        user: list[UserORM] = list(result.scalars().all())

        return user