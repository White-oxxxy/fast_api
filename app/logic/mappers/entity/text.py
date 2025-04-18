from dataclasses import dataclass

from domain.entities.text import Tag, Text
from infra.pg.models.user import TextORM, TagORM


@dataclass
class GetTextFromORM:
    def execute(self, text: TextORM) -> Text:
        return Text(
            oid=text.oid,
            value=text.value,
            tags=self._get_tags(tags=text.tags)
        )

    @staticmethod
    def _get_tags(tags: list[TagORM]) -> list[Tag]:
        return [Tag(oid=tag.oid, name=tag.name) for tag in tags]


class GetTagFromORM:
    @staticmethod
    def execute(tag: TagORM) -> Tag:
        return Tag(
            oid=tag.oid,
            name=tag.name
        )