from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.text import (
    Text,
    Tag,
)
from domain.repositories.base import IBaseRepositoryORM


class ITextTagCRUDRepositoryORM(IBaseRepositoryORM, ABC):
    @abstractmethod
    async def get_text_by_oid(self, required_oid: UUID) -> Text | None: ...

    @abstractmethod
    async def add_text(self, text: Text) -> None: ...

    @abstractmethod
    async def get_tag_by_oid(self, required_oid: UUID) -> Tag | None: ...

    @abstractmethod
    async def add_tags(self, tags: list[Tag], text_oid: UUID) -> Text: ...


class ITextTagQueryRepositoryORM(IBaseRepositoryORM, ABC):
    @abstractmethod
    async def find_by_tag_name(self, name: str) -> list[Text]: ...

    @abstractmethod
    async def search_by_value_fragment(self, fragment: str) -> list[Text]: ...

    @abstractmethod
    async def get_all_tags(self) -> list[Tag]: ...
