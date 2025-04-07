from dto.text import TextCreate, TagCreate
from infra.pg.models.user import TagORM, TextORM


class TextCreateToORM:
    def execute(self, texts_create: list[TextCreate]) -> list[TextORM]:
        result: list[TextORM] = []
        for text in texts_create:
            text_orm = self._create_text_orm(text)
            result.append(text_orm)
        return result

    @staticmethod
    def _create_text_orm(text: TextCreate) -> TextORM:
        text_orm = TextORM(value=text.value, uploader_name=text.uploader_name)
        return text_orm


class CreateTagToORM:
    def execute(self, tags_create: list[TagCreate]) -> list[TagORM]:
        result: list[TagORM] = []
        for tag in tags_create:
            tag_orm = self._create_tag_orm(tag)
            result.append(tag_orm)
        return result

    @staticmethod
    def _create_tag_orm(tag: TagCreate) -> TagORM:
        tag_orm = TagORM(name=tag.name, uploader_name=tag.uploader_name)
        return tag_orm
