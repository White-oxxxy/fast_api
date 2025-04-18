from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from dataclasses import dataclass
from uuid import UUID

from domain.services.text import ITextService, ITagService
from domain.entities.text import Text, Tag, TextInput, TagInput
from logic.mappers.entity.text import GetTextFromORM, GetTagFromORM
from infra.pg.database import Database
from infra.pg.repository.text import TextTagRepositoryORM
from infra.pg.models.user import TagORM, TextORM
from dto.text.text import TextCreate, TagCreate
from .mapper.to_create_dto import TextInputToTextCreate, TagInputToTagCreate


@dataclass
class TextTagService(ITextService, ITagService):
    database: Database

    async def create_text(self, text: TextInput) -> Text:
        async with self.database.async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            text_create: TextCreate = TextInputToTextCreate().execute(text=text)
            tags_orm: list[TagORM] = []
            for tag in text_create.tags:
                tag_orm: TagORM | None = await repo.get_tag(tag.name)
                if tag_orm:
                    tags_orm.append(tag_orm)
                    continue

                try:
                    tag_orm: TagORM = await repo.create_tag(tag)
                    tags_orm.append(tag_orm)
                    await repo.flush()
                except IntegrityError:
                    tag_orm: TagORM | None = await repo.get_tag(tag.name)
                    if tag_orm:
                        tags_orm.append(tag_orm)
                    else:
                        raise

            text_orm: TextORM = TextORM(
                value=text_create.value,
                uploader_name=text_create.uploader_name,
                tags=tags_orm
            )
            repo.save(text_orm)
            await repo.commit()

            return GetTextFromORM().execute(text=text_orm)

    async def get_text_by_value(self, text: TextInput) -> Text | None:
        async with self.database.read_only_async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            text_create: TextCreate = TextInputToTextCreate().execute(text=text)
            text_orm: TextORM | None = await repo.get_text(value=text_create.value)
            if not text_orm:
                return None

            return GetTextFromORM().execute(text=text_orm)

    async def get_text_or_create(self, text: TextInput) -> Text:
        async with self.database.async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            text_create: TextCreate = TextInputToTextCreate().execute(text=text)
            text_orm: TextORM | None = await repo.get_text(value=text_create.value)
            if not text_orm:
                text_dto: Text = await self.create_text(text=text)
                return text_dto

            return GetTextFromORM().execute(text=text_orm)

    async def get_texts_by_text(self, text: TextInput) -> list[Text]:
        async with self.database.read_only_async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            text_create: TextCreate = TextInputToTextCreate().execute(text=text)
            texts_orm: list[TextORM] = await repo.get_texts_by_text(value=text_create.value)
            texts_dto: list[Text] = []
            for text in texts_orm:
                texts_dto.append(GetTextFromORM().execute(text))

            return texts_dto

    async def get_texts_by_tag(self, tag: TagInput) -> list[Text]:
        async with self.database.read_only_async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            tag_create: TagCreate = TagInputToTagCreate.execute(tag)
            texts_orm: list[TextORM] = await repo.get_texts_by_tag(name=tag_create.name)
            texts_dto: list[Text] = []
            for text in texts_orm:
                texts_dto.append(GetTextFromORM().execute(text))

            return texts_dto

    async def get_all_tags_name(self) -> list[Tag]:
        async with self.database.read_only_async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            tags_orm: list[TagORM] = await repo.get_all_tag_names()
            tags_dto: list[Tag] = []
            for tag in tags_orm:
                tags_dto.append(GetTagFromORM.execute(tag=tag))

            return tags_dto

    async def _get_text_by_oid(self, required_oid: UUID) -> Text | None:
        async with self.database.read_only_async_session as session:
            repo: TextTagRepositoryORM = self.__get_repo(session=session)
            text: TextORM | None = await repo.get_text_by_oid(required_oid=required_oid)
            return GetTextFromORM().execute(text)

    @staticmethod
    def __get_repo(session: AsyncSession) -> TextTagRepositoryORM:
        return TextTagRepositoryORM(session=session)
