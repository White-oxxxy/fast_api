from dataclasses import dataclass

from domain.entities.text import Text, Tag
from domain.values.text import TextValue, TagName
from domain.values.user import Username
from infra.pg.models.user import TextORM, TagORM


@dataclass
class TextToTextORMMapper:
    def execute(self, text: Text) -> TextORM:
        return TextORM(
            value=TextValue(text.value).as_generic_type(),
            uploader_name=Username(text.uploader_name).as_generic_type(),
            tags=self._get_tags(tags=text.tags)
        )

    @staticmethod
    def _get_tags(tags: list[Tag]) -> list[TagORM]:
        return [
            TagORM(
                name=TagName(tag.name).as_generic_type(),
                uploader_name=Username(tag.uploader_name).as_generic_type()
            )
            for tag in tags
        ]


@dataclass
class TagToTagORMMapper:
    @staticmethod
    def execute(tag: Tag) -> TagORM:
        return TagORM(
            name=TagName(tag.name).as_generic_type(),
            uploader_name=Username(tag.uploader_name).as_generic_type()
        )