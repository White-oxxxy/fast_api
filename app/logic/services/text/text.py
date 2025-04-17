from sqlalchemy.ext.asyncio import AsyncSession

from dataclasses import dataclass

from domain.services.text import ITextService, ITagService
from domain.entities.text import Text, Tag, TextInput, TagInput
from logic.mappers.entity.text import GetTextFromORM
from infra.pg.database import Database
from infra.pg.repository.text import TextTagRepositoryORM
from infra.pg.models.user import TagORM, TextORM
from dto.text.text import TextCreate, TagCreate
from .mapper.to_create_dto import TextInputToTextCreate


@dataclass
class TextTagService(ITextService, ITagService):
    database: Database

    async def create_text(self, text: TextInput) -> Text:
        async with self.database.async_session as session:
            repo = self.__get_repo(session=session)

            text_create: TextCreate = TextInputToTextCreate().execute(text=text)

            tags_orm: list[TagORM] = []

            for tag in text_create.tags:
                tag_orm: TagORM | None = await repo.get_tag(tag.name)
                if not tag_orm:
                    tag_orm: TagORM = await repo.create_tag(tag)
                    tags_orm.append(tag_orm)

            text_orm: TextORM = TextORM(
                value=text_create.value,
                uploader_name=text_create.uploader_name,
                tags=tags_orm
            )




    @staticmethod
    def __get_repo(session: AsyncSession) -> TextTagRepositoryORM:
        return TextTagRepositoryORM(session=session)
