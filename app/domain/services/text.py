from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.text import Text, Tag
from domain.entities.text import TextInput, TagInput


class ICreateTextService(ABC):
    @abstractmethod
    async def execute(self, text: TextInput) -> Text: ...


class IGetOrCreateTextService(ABC):
    @abstractmethod
    async def execute(self, text: TextInput) -> Text: ...


class IAddTagService(ABC):
    @abstractmethod
    async def execute(self, tag: TagInput, text_oid: UUID) -> Text: ...


class IGetOrAddTagService(ABC):
    @abstractmethod
    async def execute(self, tag: TagInput, text_oid: UUID) -> Text: ...


