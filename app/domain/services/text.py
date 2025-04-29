from abc import ABC, abstractmethod

from domain.entities.text import Text
from domain.repositories.text import ITextTagCRUDRepositoryORM


class ICreateTextService(ABC):
    repo: ITextTagCRUDRepositoryORM

    @abstractmethod
    async def execute(self, text: Text) -> Text: ...


class IGetOrCreateTextService(ABC):
    repo: ITextTagCRUDRepositoryORM
    create_text_service: ICreateTextService

    @abstractmethod
    async def execute(self, text: Text) -> Text: ...



