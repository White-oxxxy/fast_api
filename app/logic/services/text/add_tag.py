from dataclasses import dataclass

from uuid import UUID

from domain.services.text import IAddTagsService
from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.exeptions.infra.text import TextDoesntCreatedException
from domain.entities.text import (
    Text,
    Tag,
)


@dataclass
class AddTagService(IAddTagsService):
    repo: ITextTagCRUDRepositoryORM

    async def execute(self, tags: list[Tag], text_oid: UUID) -> None:
        for tag in tags:
            text_entity: Text | None = await self.repo.add_tag(tag=tag, text_oid=text_oid)
            if not text_entity:
                raise TextDoesntCreatedException

            await self.repo.flush()
