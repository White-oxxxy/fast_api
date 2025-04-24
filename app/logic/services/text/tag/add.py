from sqlalchemy.exc import IntegrityError

from dataclasses import dataclass

from uuid import UUID

from domain.services.text import IAddTagService
from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.exeptions.infra.text import (
    TagAlreadyExistedException,
    TextDoesntCreatedException,
)
from domain.entities.text import (
    Text,
    TagInput
)


@dataclass
class AddTagService(IAddTagService):
    repo: ITextTagCRUDRepositoryORM

    async def execute(self, tag: TagInput, text_oid: UUID) -> Text:
        try:
            text_entity: Text | None = await self.repo.add_tag(tag=tag, text_oid=text_oid)
            if not text_entity:
                raise TextDoesntCreatedException

            await self.repo.flush()

            return text_entity
        except IntegrityError:
            raise TagAlreadyExistedException()