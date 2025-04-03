from domain.entities.user import Tag, Text
from infra.pg.models.user import TextORM, TagORM


class GetTagFromORM:
    @staticmethod
    def execute(tag: TagORM) -> Tag:
        tag_entity = Tag(
            oid=tag.oid,
            name=tag.name,
            uploader_name=tag.uploader_name
        )
        return tag_entity


class GetTextFromORM:
    def execute(self, text: TextORM) -> Text:
        tag_entity: list[Tag] = [
            self._get_tags(tag) for tag in text.tags
        ]
        text_entity = Text(
            oid=text.oid,
            value=text.value,
            uploader_name=text.uploader_name,
            tags=tag_entity
        )
        return text_entity

    @staticmethod
    def _get_tags(tag: TagORM) -> Tag:
        return Tag(
            oid=tag.oid,
            name=tag.name,
            uploader_name=tag.uploader_name
        )