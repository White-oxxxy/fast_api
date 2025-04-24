from sqlalchemy.ext.asyncio import AsyncSession

from dataclasses import dataclass
from uuid import UUID

from domain.entities.token import TokenInput, Token
from domain.services.auth import ITokenService
from infra.pg.database import Database
from infra.pg.models.user import RefreshTokenORM, UserORM
from infra.pg.repository.token import RefreshTokenRepositoryORM
from infra.pg.repository.user import UserRepositoryORM
from dto.token.token import RefreshTokenCreate
from logic.services.auth.mapper.to_create_dto import RefreshTokenInputToRefreshTokenCreate


@dataclass
class TokenService(ITokenService):
    database: Database

    async def create(self, token: TokenInput) -> Token:
        async with self.database.async_session as session:
            token_repo: RefreshTokenRepositoryORM = self.__get_token_repo(session=session)
            user_repo: UserRepositoryORM = self.__get_user_repo(session=session)
            user: UserORM = await user_repo.get_by_username(username=token.username)

    async def get(self, token: TokenInput) -> Token | None:
        async with self.database.read_only_async_session as session:
            token_repo: RefreshTokenRepositoryORM = self.__get_token_repo(session=session)

    async def get_or_create(self, token: TokenInput) -> Token:
        async with self.database.async_session as session:
            token_repo: RefreshTokenRepositoryORM = self.__get_token_repo(session=session)

    async def delete(self, token: TokenInput) -> None:
        async with self.database.async_session as session:
            token_repo: RefreshTokenRepositoryORM = self.__get_token_repo(session=session)

    async def _get_by_oid(self, required_oid: UUID) -> Token | None:
        async with self.database.read_only_async_session as session:
            token_repo: RefreshTokenRepositoryORM = self.__get_token_repo(session=session)

    @staticmethod
    def __get_token_repo(session: AsyncSession) -> RefreshTokenRepositoryORM:
        return RefreshTokenRepositoryORM(session)

    @staticmethod
    def __get_user_repo(session: AsyncSession) -> UserRepositoryORM:
        return UserRepositoryORM(session)