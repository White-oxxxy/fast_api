from sqlalchemy import Result, Select, select
from sqlalchemy.orm import selectinload, joinedload
from uuid import UUID

from dto.text import TextCreate, TagCreate
from .base import BaseRepositoryORM
from infra.pg.models.user import TagORM, TextORM, UserORM
from infra.pg.models.associative import TextTagORM, UserTagORM, UserTextORM


class TextRepositoryORM(BaseRepositoryORM):
    async def get_text_by_id(self, required_id: int) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_id)
        return text

    async def get_text_by_oid(self, required_oid: UUID) -> TextORM | None:
        text: TextORM | None = await self.session.get(TextORM, required_oid)
        return text

    async def create_text(self, text: TextCreate) -> TextORM:
        text = TextORM(**text.model_dump())
        self.session.add(text)
        return text

    async def get_text(self, value: str) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = select(TextORM).where(TextORM.value == value)
        text: TextORM | None = await self.session.scalar(stmt)
        if not text:
            return None

        return text

    async def get_tag_by_id(self, required_id: int) -> TagORM | None:
        tag: TagORM | None = await self.session.get(TagORM, required_id)
        return tag

    async def get_tag_by_oid(self, required_oid: UUID) -> TagORM | None:
        tag: TagORM | None = await self.session.get(TagORM, required_oid)
        return tag

    async def add_tag(self, tag: TagCreate, text_id: int) -> TextORM | None:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .where(TextORM.pk == text_id)
            .options(selectinload(TextORM.tags))
        )
        result: Result = await self.session.execute(stmt)
        text: TextORM | None = result.scalars().first()
        if text:
            tag = TagORM(**tag.model_dump())
            text.tags.append(tag)
            self.session.add(text)
        return text

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


class TextTagRepositoryORM(BaseRepositoryORM):
    async def get_by_tag(self, name: str) -> list[TextORM]:
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

    async def get_by_text(self, value: str) -> list[TextORM]:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_oid == TextORM.oid)
            .filter(TextORM.value.like("%" + value + "%"))
        )
        result: Result[tuple[TextORM]] = await self.session.execute(stmt)
        text: list[TextORM] = list(result.scalars().all())
        return text


# class UserTagRepositoryORM(BaseRepositoryORM):
#     async def get_by_username(self, username: str) -> list[TagORM]:
#         stmt: Select[tuple[TagORM]] = (
#             select(TagORM)
#             .join(UserTagORM, UserTagORM.tag_oid == TagORM.oid)
#             .join(UserORM, UserTagORM.user_oid == UserORM.oid)
#             .where(UserORM.username == username)
#         )
#         result: Result[tuple[TagORM]] = await self.session.execute(stmt)
#         tags: list[TagORM] = list(result.scalars().all())
#         return tags
#
#
# class UserTextRepositoryORM(BaseRepositoryORM):
#     async def get_by_username(self, username: str) -> list[TextORM]:
#         stmt: Select[tuple[TextORM]] = (
#             select(TextORM)
#             .join(UserTextORM, UserTextORM.text_oid == TextORM.oid)
#             .join(UserORM, UserTextORM.user_oid == UserORM.oid)
#             .where(UserORM.username == username)
#         )
#         result: Result[tuple[TextORM]] = await self.session.execute(stmt)
#         texts: list[TextORM] = list(result.scalars().all())
#         return texts