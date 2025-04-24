from dataclasses import dataclass

from uuid import UUID

from domain.services.text import (
    IGetOrAddTagService,
    IAddTagService,
)
from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.exeptions.infra.text import (
    TagAlreadyExistedException,
    TextDoesntCreatedException,
)
from domain.entities.text import (
    Text,
    Tag,
    TagInput
)


@dataclass
class GetOrAddTagService(IGetOrAddTagService):
    repo: ITextTagCRUDRepositoryORM
    add_tag_service: IAddTagService

    async def execute(self, tag: TagInput, text_oid: UUID) -> Text:
        tag_name: str = tag.name.as_generic_type()

        tag_entity: Tag = await self.repo.get_tag(name=tag_name)

        if not tag_entity:
            try:
                text_entity: Text = await self.add_tag_service.execute(tag=tag, text_oid=text_oid)

                return text_entity

            except TextDoesntCreatedException:
                raise TextDoesntCreatedException()

            except TagAlreadyExistedException:
                tag_entity: Tag = await self.repo.get_tag(name=tag_name)
                if tag_entity:
                    raise TagAlreadyExistedException()
        else:
            raise TagAlreadyExistedException()