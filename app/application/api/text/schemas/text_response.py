from pydantic import BaseModel


class GetTagSchema(BaseModel):
    name: str

class GetTagsSchema(BaseModel):
    names: list[GetTagSchema]

class GetTextSchema(BaseModel):
    value: str

class GetTextsSchema(BaseModel):
    values: list[GetTextSchema]