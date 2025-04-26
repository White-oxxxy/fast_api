from sqlalchemy.exc import IntegrityError

from dataclasses import dataclass

from domain.entities.user import User
from domain.services.user import ICreateUserService
from domain.exeptions.infra.user import UserAlreadyExistedException
from domain.repositories.user import IUserRepositoryORM


@dataclass
class CreateUserService(ICreateUserService):
    repo: IUserRepositoryORM

    async def execute(self, user: User) -> User:
        try:
            user_entity: User = await self.repo.create(user=user)

            await self.repo.flush()

            return user_entity
        except IntegrityError:
            raise UserAlreadyExistedException()
