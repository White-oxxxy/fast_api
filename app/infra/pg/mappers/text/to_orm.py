from domain.entities.text import TextInput, TagInput
from domain.values.text import TextValue, TagName
from domain.values.user import Username
from infra.pg.models.user import TextORM, TagORM


class TextInputToTextORM:
    @staticmethod
    def execute(text: TextInput) -> TextORM:
        return TextORM(
            value=TextValue(text.value).as_generic_type(),
            uploader_name=Username(text.uploader_name).as_generic_type(),
        )


class TagInputToTagORM:
    @staticmethod
    def execute(tag: TagInput) -> TagORM:
        return TagORM(
            name=TagName(tag.name).as_generic_type(),
            uploader_name=Username(tag.uploader_name).as_generic_type()
        )