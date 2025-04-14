from pydantic import BaseModel


class TagSchema(BaseModel):
    name: str

class CreateTagSchema(BaseModel):
    name: str
    uploader_name: str

class TextSchema(BaseModel):
    value: str
    tags: list[TagSchema]

class CreateTextSchema(BaseModel):
    value: str
    uploader_name: str