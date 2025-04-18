from abc import ABC
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from infra.pg.models.base import BaseORM


@dataclass
class BaseRepositoryORM(ABC):
    session: AsyncSession

    async def commit(self) -> None:
        await self.session.commit()

    async def flush(self) -> None:
        await self.session.flush()

    def save(self, instance: BaseORM) -> None:
        self.session.add(instance)
