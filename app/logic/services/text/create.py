from sqlalchemy.exc import IntegrityError

from dataclasses import dataclass

from domain.services.text import (
    ICreateTextService,
    IGetOrAddTagService,
)
from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.entities.text import (
    Text,
    Tag,
    TextInput,
)
from domain.exeptions.infra.text import (
    TextAlreadyExistedException,
    TagAlreadyExistedException,
    TextDoesntCreatedException,
)


@dataclass
class CreateTextService(ICreateTextService):
    repo: ITextTagCRUDRepositoryORM
    get_or_add_tag_service: IGetOrAddTagService

    async def execute(self, text: TextInput) -> Text:
        username: str = text.uploader_name.as_generic_type()
        for tag in text.tags:
            try:
                text_entity: Text = await self.get_or_add_tag_service.execute(tag=tag, text_oid=text.oid)
            except TextDoesntCreatedException:
                raise TextDoesntCreatedException()







