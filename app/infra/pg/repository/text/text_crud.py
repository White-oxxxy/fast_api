from sqlalchemy import Select, select
from sqlalchemy.orm import joinedload
from uuid import UUID

from domain.repositories.text import ITextTagCRUDRepositoryORM
from domain.entities.text import (
    Text,
    Tag,
    TagInput,
    TextInput,
)
from infra.pg.mappers.text import *
from infra.pg.repository.base import BaseRepositoryORM
from infra.pg.models.user import (
    TagORM,
    TextORM,
)


class TextTagCRUDRepositoryORM(BaseRepositoryORM, ITextTagCRUDRepositoryORM):
    async def get_text_by_oid(self, required_oid: UUID) -> Text | None:
        stmt = (
            select(TextORM)
            .where(TextORM.oid == required_oid)
            .options(joinedload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        text_entity: Text = GetTextFromORM().execute(text=text)
        return text_entity

    async def get_text(self, value: str) -> Text | None:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.value == value)
            .options(joinedload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        text_entity: Text = GetTextFromORM().execute(text=text)
        return text_entity

    async def create_text(self, text: TextInput) -> Text:
        text_orm: TextORM = TextInputToTextORM.execute(text=text)
        self.session.add(text_orm)
        text_entity: Text = GetTextFromORM().execute(text=text_orm)
        return text_entity

    async def get_tag_by_oid(self, required_oid: UUID) -> Tag | None:
        tag: TagORM | None = await self.session.get(TagORM, required_oid)
        if not tag:
            return None

        tag_entity: Tag = GetTagFromORM.execute(tag=tag)
        return tag_entity

    async def add_tag(self, tag: TagInput, text_oid: UUID) -> Text:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.oid == text_oid)
            .options(joinedload(TextORM.tags))
        )
        text: TextORM | None = await self.session.scalar(stmt)
        if text:
            tag_orm: TagORM = TagInputToTagORM.execute(tag=tag)
            text.tags.append(tag_orm)
            self.session.add(text)

        text_entity: Text = GetTextFromORM().execute(text=text)

        return text_entity

    async def get_tag(self, name: str) -> Tag | None:
        stmt: Select[tuple[TagORM]] = select(TagORM).where(TagORM.name == name)
        tag: TagORM | None = await self.session.scalar(stmt)
        if not tag:
            return None

        tag_entity: Tag = GetTagFromORM.execute(tag=tag)
        return tag_entity
