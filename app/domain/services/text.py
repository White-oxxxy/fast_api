from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.text import Text, Tag
from domain.repositories.text import ITextTagCRUDRepositoryORM


class IAddTagsService(ABC):
    repo: ITextTagCRUDRepositoryORM

    @abstractmethod
    async def execute(self, tags: list[Tag], text_oid: UUID) -> None: ...


class ICreateTextService(ABC):
    repo: ITextTagCRUDRepositoryORM
    add_tags_service: IAddTagsService

    @abstractmethod
    async def execute(self, text: Text) -> Text: ...


class IGetOrCreateTextService(ABC):
    repo: ITextTagCRUDRepositoryORM
    create_text_service: ICreateTextService

    @abstractmethod
    async def execute(self, text: Text) -> Text: ...



