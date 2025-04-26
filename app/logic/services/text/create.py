from sqlalchemy.exc import IntegrityError

from dataclasses import dataclass

from domain.services.text import (
    ICreateTextService,
    IAddTagsService,
)
from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.entities.text import (
    Text,
    Tag,
)
from domain.exeptions.infra.text import (
    TextAlreadyExistedException,
    TextDoesntCreatedException,
)


@dataclass
class CreateTextService(ICreateTextService):
    repo: ITextTagCRUDRepositoryORM
    add_tags_service: IAddTagsService

    async def execute(self, text: Text) -> Text:
        tags: list[Tag] = []
        for tag in text.tags:
            checked_tag: Tag | None = await self.repo.get_tag_by_oid(tag.oid)
            if not checked_tag:
                tags.append(tag)

        new_text_entity = Text(
            value=text.value,
            uploader_name=text.uploader_name,
            tags=tags
        )
        try:
            await self.repo.add_text(new_text_entity)
            await self.repo.flush()
        except IntegrityError:
            raise TextAlreadyExistedException()

        try:
            await self.add_tags_service.execute(tags=text.tags, text_oid=text.oid)
        except TextDoesntCreatedException:
            raise

        text_entity: Text = await self.repo.get_text_by_oid(new_text_entity.oid)

        return text_entity












