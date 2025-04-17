from dataclasses import dataclass

from application.api.text.schemas.text import CreateTextSchema
from dto.text.text_response import Text as TextDto
from dto.text.text_response import Tag as TagDto


@dataclass
class FastAPIRequestToTextDTO:
    def execute(self, request: CreateTextSchema) -> TextDto:
        return TextDto(
            value=request.value,
            uploader_name=request.uploader_name,
            tags=self._request_to_dto(tags=request.tags)
        )

    @staticmethod
    def _request_to_dto(tags: list[CreateTextSchema.tags]) -> list[TagDto]:
        return [TagDto(name=tag.name, uploader_name=tag.uploader_name) for tag in tags]