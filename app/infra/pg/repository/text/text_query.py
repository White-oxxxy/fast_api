from sqlalchemy import (
    Result,
    Select,
    select,
)
from sqlalchemy.orm import joinedload

from domain.entities.text import (
    Text,
    Tag,
)
from infra.pg.repository.base import BaseRepositoryORM
from domain.repositories.text import ITextTagQueryRepositoryORM
from infra.pg.models.user import TextORM, TagORM
from infra.pg.models.associative import TextTagORM
from infra.pg.mappers.text import *


class TextTagQueryRepositoryORM(BaseRepositoryORM, ITextTagQueryRepositoryORM):
    async def find_by_tag_name(self, name: str) -> list[Text]:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_oid == TextORM.oid)
            .join(TagORM, TextTagORM.tag_oid == TagORM.oid)
            .where(TagORM.name == name)
            .options(joinedload(TextORM.tags))
        )
        result: Result[tuple[TextORM]] = await self.session.execute(stmt)
        text_orms: list[TextORM] = list(result.unique().scalars().all())
        text_entities: list[Text] = []
        for text_orm in text_orms:
            text_entities.append(GetTextFromORMMapper().execute(text=text_orm))
        return text_entities

    async def search_by_value_fragment(self, fragment: str) -> list[Text]:
        stmt: Select[tuple[TextORM]] = (
            select(TextORM)
            .join(TextTagORM, TextTagORM.text_oid == TextORM.oid)
            .filter(TextORM.value.like("%" + fragment + "%"))
            .options(joinedload(TextORM.tags))
        )
        result: Result[tuple[TextORM]] = await self.session.execute(stmt)
        text_orms: list[TextORM] = list(result.scalars().all())
        text_entities: list[Text] = []
        for text_orm in text_orms:
            text_entities.append(GetTextFromORMMapper().execute(text=text_orm))
        return text_entities

    async def get_all_tags(self) -> list[Tag]:
        stmt: Select[tuple[TagORM]] = (
            select(TagORM)
        )
        result: Result[tuple[TagORM]] = await self.session.execute(stmt)
        tag_orms: list[TagORM] = list(result.scalars().all())
        tag_entities: list[Tag] = []
        for tag_orm in tag_orms:
            tag_entities.append(GetTagFromORMMapper.execute(tag=tag_orm))
        return tag_entities
