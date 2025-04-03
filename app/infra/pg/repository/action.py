from sqlalchemy import Result, Select, select
from sqlalchemy.orm import selectinload, joinedload
from uuid import UUID

from dto.action import ActionCreate
from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM, ActionORM
from infra.pg.models.associative import UserActionORM


class ActionRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> ActionORM | None:
        action: ActionORM | None = await self.session.get(ActionORM, required_id)
        return action

    async def get_by_oid(self, required_oid: UUID) -> ActionORM | None:
        action: ActionORM | None = await self.session.get(ActionORM, required_oid)
        return action

    async def create(self, action: ActionCreate) -> ActionORM:
        action = ActionORM(**action.model_dump())
        self.session.add(action)
        return action


class UserActionRepositoryORM(BaseRepositoryORM):
    async def get_by_username(self, username: str) -> list[ActionORM]:
        stmt: Select[tuple[ActionORM]] = (
            select(ActionORM)
            .join(UserActionORM, UserActionORM.action_oid == ActionORM.oid)
            .join(UserORM, UserActionORM.user_oid == UserORM.oid)
            .where(UserORM.username == username)
        )
        result: Result[tuple[ActionORM]] = await self.session.execute(stmt)
        texts: list[ActionORM] = list(result.scalars().all())
        return texts