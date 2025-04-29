from dataclasses import dataclass

from sqlalchemy import Select, select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from uuid import UUID

from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.entities.text import (
    Text,
    Tag,
)
from domain.exeptions.infra.text import (
    TextAlreadyExistedException,
    TextDoesntCreatedException,
    TagAlreadyExistedException,
)
from infra.pg.mappers.text import (
    TextToTextORMMapper,
    TagToTagORMMapper,
    GetTagFromORMMapper,
    GetTextFromORMMapper,
)
from infra.pg.repository.base import BaseRepositoryORM
from infra.pg.models.user import (
    TagORM,
    TextORM,
)


@dataclass
class TextTagCRUDRepositoryORM(BaseRepositoryORM, ITextTagCRUDRepositoryORM):
    text_domain_to_orm_mapper: TextToTextORMMapper
    tag_domain_to_orm_mapper: TagToTagORMMapper
    text_orm_to_domain_mapper: GetTextFromORMMapper
    tag_orm_to_domain_mapper: GetTagFromORMMapper

    async def get_text_by_oid(self, required_oid: UUID) -> Text | None:
        stmt = (
            select(TextORM)
            .where(TextORM.oid == required_oid)
            .options(selectinload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        text_entity: Text = GetTextFromORMMapper().execute(text=text)
        return text_entity

    async def add_text(self, text: Text) -> None:
        text_orm: TextORM = self.text_domain_to_orm_mapper.execute(text=text)
        self.session.add(text_orm)
        try:
            await self.session.flush()
        except IntegrityError:
            raise TextAlreadyExistedException()

    async def get_tag_by_oid(self, required_oid: UUID) -> Tag | None:
        tag: TagORM | None = await self.session.get(TagORM, required_oid)
        if not tag:
            return None

        tag_entity: Tag = GetTagFromORMMapper.execute(tag=tag)
        return tag_entity

    async def add_tags(self, tags: list[Tag], text_oid: UUID) -> Text:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.oid == text_oid)
            .options(selectinload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            raise TextDoesntCreatedException()

        tags_orm: list[TagORM] = []
        for tag in tags:
            tag_orm: TagORM = self.tag_domain_to_orm_mapper.execute(tag=tag)
            tags_orm.append(tag_orm)
        text.tags.extend(tags_orm)
        self.session.add(text)

        text_entity: Text = GetTextFromORMMapper().execute(text=text)

        return text_entity
