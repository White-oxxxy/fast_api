from dataclasses import dataclass

from dto.text.text_response import Text, Tag
from dto.text.text import TextCreate, TagCreate


@dataclass
class TextDtoToTextCreate:
    def execute(self, text_dto: Text) -> TextCreate:
        return TextCreate(
            value=text_dto.value,
            uploader_name=text_dto.uploader_name,
            tags=self._get_tags(tags_dto=text_dto.tags)
        )

    @staticmethod
    def _get_tags(tags_dto: list[Tag]) -> list[TagCreate]:
        return [TagCreate(name=tag_dto.name, uploader_name=tag_dto.uploader_name) for tag_dto in tags_dto]

