from dataclasses import dataclass

from sqlalchemy import Select, select
from sqlalchemy.orm import joinedload
from uuid import UUID

from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.entities.text import (
    Text,
    Tag,
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
            .options(joinedload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        text_entity: Text = GetTextFromORMMapper().execute(text=text)
        return text_entity

    async def add_text(self, text: Text) -> None:
        text_orm: TextORM = self.text_domain_to_orm_mapper.execute(text=text)
        self.session.add(text_orm)

    async def get_tag_by_oid(self, required_oid: UUID) -> Tag | None:
        tag: TagORM | None = await self.session.get(TagORM, required_oid)
        if not tag:
            return None

        tag_entity: Tag = GetTagFromORMMapper.execute(tag=tag)
        return tag_entity

    async def add_tag(self, tag: Tag, text_oid: UUID) -> Text | None:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.oid == text_oid)
            .options(joinedload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        tag_orm: TagORM = self.tag_domain_to_orm_mapper.execute(tag=tag)
        text.tags.append(tag_orm)
        self.session.add(text)

        text_entity: Text = GetTextFromORMMapper().execute(text=text)

        return text_entity
