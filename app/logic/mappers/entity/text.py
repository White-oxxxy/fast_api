from domain.entities.text import Tag, Text
from infra.pg.models.user import TextORM, TagORM


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
