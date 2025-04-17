from dataclasses import dataclass

from dto.text.text import TextCreate, TagCreate
from infra.pg.models.user import TagORM, TextORM

@dataclass
class TextCreateToORM:
    def execute(self, text: TextCreate) -> TextORM:
        return TextORM(
            value=text.value,
            uploader_name=text.uploader_name,
            tags=self._get_tags_orm(tags=text.tags)
        )

    @staticmethod
    def _get_tags_orm(tags: list[TagCreate]) -> list[TagORM]:
        return [TagORM(name=tag.name, uploader_name=tag.uploader_name) for tag in tags]
