from dataclasses import dataclass

from domain.entities.user import User, UserInput
from domain.services.user import IGetOrCreateUserService, ICreateUserService
from domain.exeptions.infra.user import UserAlreadyExistedException
from domain.repositories.user import IUserRepositoryORM


@dataclass
class GetOrCreateUserService(IGetOrCreateUserService):
    repo: IUserRepositoryORM
    create_user_service: ICreateUserService

    async def execute(self, user: UserInput) -> User:
        username: str = user.username.as_generic_type()

        user_entity: User = await self.repo.get_by_username(username=username)
        if user_entity:
            return user_entity

        try:
            user_entity: User = await self.create_user_service.execute(user=user)

            await self.repo.commit()

            return user_entity
        except UserAlreadyExistedException:
            user_entity: User = await self.repo.get_by_username(username=username)
            if user_entity:
                return user_entity
            else:
                raise UserAlreadyExistedException()