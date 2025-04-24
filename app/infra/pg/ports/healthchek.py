from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.ports.healthchek import IDatabaseHealthchekPort


class DatabaseHealthchekPort(IDatabaseHealthchekPort):
    session: AsyncSession

    async def ping(self) -> bool:
        try:
            result = await self.session.execute(select(1))
            return result.scalar() == 1
        except SQLAlchemyError:
            return False
