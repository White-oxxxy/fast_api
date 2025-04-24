from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from domain.repositories.base import IBaseRepositoryORM


@dataclass
class BaseRepositoryORM(IBaseRepositoryORM):
    session: AsyncSession

    async def commit(self) -> None:
        await self.session.commit()

    async def flush(self) -> None:
        await self.session.flush()