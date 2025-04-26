from domain.entities.text import Tag, Text
from domain.values.text import (
    TagName,
    TextValue,
)
from domain.values.user import Username
from infra.pg.models.user import (
    TextORM,
    TagORM,
)


class GetTextFromORMMapper:
    def execute(self, text: TextORM) -> Text:
        return Text(
            oid=text.oid,
            value=TextValue(text.value),
            uploader_name=Username(text.uploader_name),
            tags=self._get_tags(tags=text.tags)
        )

    @staticmethod
    def _get_tags(tags: list[TagORM]) -> list[Tag]:
        return [Tag(oid=tag.oid, name=TagName(tag.name), uploader_name=Username(tag.uploader_name)) for tag in tags]


class GetTagFromORMMapper:
    @staticmethod
    def execute(tag: TagORM) -> Tag:
        return Tag(
            oid=tag.oid,
            name=TagName(tag.name),
            uploader_name=Username(tag.uploader_name)
        )