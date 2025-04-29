from dataclasses import dataclass

from domain.entities.user import User
from domain.services.user import IGetOrCreateUserService
from domain.exeptions.infra.user import (
    UserAlreadyExistedException,
    RoleDoesntCreatedException,
)
from domain.repositories.user import IUserRepositoryORM


@dataclass
class GetOrCreateUserService(IGetOrCreateUserService):
    repo: IUserRepositoryORM

    async def execute(self, user: User) -> User:
        user_entity: User = await self.repo.get_by_oid(required_oid=user.oid)
        if user_entity:
            return user_entity

        try:
            user_entity: User = await self.repo.create(user=user)

            await self.repo.commit()

            return user_entity
        except UserAlreadyExistedException:
            user_entity: User = await self.repo.get_by_oid(required_oid=user.oid)
            if user_entity:
                return user_entity
            else:
                raise
        except RoleDoesntCreatedException:
            raise