from sqlalchemy import Result, Select, select
from sqlalchemy.orm import selectinload
from uuid import UUID

from .base import BaseRepositoryORM
from infra.pg.models.user import TagORM, TextORM


class TextRepositoryORM(BaseRepositoryORM):
    async def get_by_id(self, required_id: int) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_id)

        return text

    async def create_text(self, value: str, uploader_id: int) -> TextORM:
        text = TextORM(value=value, uploader_id=uploader_id)
        self.session.add(text)
        await self.session.flush()

        return text

    async def get_text(self, value: str) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = select(TextORM).where(TextORM.value == value)
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        return text

    async def add_tag(self, tag: TagORM, text_id: int) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.id == text_id)
            .options(selectinload(TextORM.tags))
        )
        result: Result = await self.session.execute(stmt)
        text: TextORM | None = result.scalars().first()
        if text:
            text.tags.append(tag)
            self.session.add(text)

        return text

    async def add_tags(self, tags: list[TagORM], text_id: int) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.id == text_id)
            .options(selectinload(TextORM.tags))
        )
        result: Result = await self.session.execute(stmt)
        text: TextORM | None = result.scalars().first()
        if text:
            text.tags.extend(tags)
            self.session.add(text)

        return text

    async def get_tag_by_name(self, name: str) -> TagORM | None:
        stmt: Select[tuple[TagORM]] = select(TagORM).where(TagORM.name == name)
        tag: TagORM | None = await self.session.scalar(stmt)
        if not tag:
            return None

        return tag

    async def get_all_tag_names(self) -> list[TagORM.name]:
        stmt: Select[tuple[TagORM.name]] = select(TagORM.name)
        result: Result = await self.session.execute(stmt)
        tags: list[TagORM.name] = list(result.scalars().all())

        return tags