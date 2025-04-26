from dataclasses import dataclass

from domain.services.text import (
    ICreateTextService,
    IGetOrCreateTextService,
)
from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.entities.text import Text
from domain.exeptions.infra.text import TextAlreadyExistedException


@dataclass
class GetOrCreateTextService(IGetOrCreateTextService):
    repo: ITextTagCRUDRepositoryORM
    create_text_service: ICreateTextService

    async def execute(self, text: Text) -> Text:
        text_entity: Text = await self.repo.get_text_by_oid(required_oid=text.oid)
        if text_entity:
            return text_entity

        try:
            text_entity: Text = await self.create_text_service.execute(text=text)

            await self.repo.commit()

            return text_entity
        except TextAlreadyExistedException:
            existing_text = await self.repo.get_text_by_oid(required_oid=text.oid)
            if existing_text:
                return existing_text
            raise
