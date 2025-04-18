from abc import ABC, abstractmethod

from domain.entities.text import Text, Tag, TextInput


class ITextService(ABC):
    @abstractmethod
    async def create_text(self, text: TextInput) -> Text: ...

    @abstractmethod
    async def get_text_by_value(self, text: TextInput) -> Text | None: ...

    @abstractmethod
    async def get_text_or_create(self, text: TextInput) -> Text: ...

    @abstractmethod
    async def get_texts_by_text(self, text: TextInput) -> list[Text]: ...

    @abstractmethod
    async def get_texts_by_tag(self, text: TextInput) -> list[Text]: ...


class ITagService(ABC):
    @abstractmethod
    async def get_all_tags_name(self) -> list[Tag.name]: ...
