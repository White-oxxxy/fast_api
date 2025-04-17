from uuid import UUID

from dto.action import ActionCreate
from .base import BaseRepositoryORM
from infra.pg.models.user import UserORM, ActionORM


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
