from sqlalchemy import Result, Select, select
from sqlalchemy.orm import joinedload
from uuid import UUID

from dto.text.text import TagCreate
from .base import BaseRepositoryORM
from infra.pg.models.user import TagORM, TextORM
from infra.pg.models.associative import TextTagORM


class TextTagRepositoryORM(BaseRepositoryORM):
    async def get_text_by_oid(self, required_oid: UUID) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_oid)
        return text

    async def get_text(self, value: str) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = select(TextORM).where(TextORM.value == value)
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        return text

    async def get_tag_by_oid(self, required_oid: UUID) -> TagORM | None:
        tag: TagORM | None = await self.session.get(TagORM, required_oid)
        return tag

    async def create_tag(self, tag: TagCreate) -> TagORM:
        tag = TagORM(**tag.model_dump())
        self.session.add(tag)
        return tag

    async def get_tag(self, name: str) -> TagORM | None:
        stmt: Select[tuple[TagORM]] = select(TagORM).where(TagORM.name == name)
        tag: TagORM | None = await self.session.scalar(stmt)
        if not tag:
            return None
        return tag

    async def get_all_tag_names(self) -> list[TagORM.name]:
        stmt: Select[tuple[TagORM.name]] = select(TagORM.name)
        result: Result[tuple[TagORM.name]] = await self.session.execute(stmt)
        tags: list[TagORM.name] = list(result.scalars().all())
        return tags

    async def get_texts_by_tag(self, name: str) -> list[TextORM]:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_oid == TextORM.oid)
            .join(TagORM, TextTagORM.tag_oid == TagORM.oid)
            .where(TagORM.name == name)
            .options(joinedload(TextORM.tags))
        )
        result: Result[tuple[TextORM]] = await self.session.execute(stmt)
        text: list[TextORM] = list(result.unique().scalars().all())
        return text

    async def get_texts_by_text(self, value: str) -> list[TextORM]:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_oid == TextORM.oid)
            .filter(TextORM.value.like("%" + value + "%"))
        )
        result: Result[tuple[TextORM]] = await self.session.execute(stmt)
        text: list[TextORM] = list(result.scalars().all())
        return text