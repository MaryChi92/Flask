from pydantic import BaseModel
from blog.schemas.article import ResponseArticleModel


class QueryTagModel(BaseModel):
    id: int


class ResponseTagModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ResponseTagsModel(BaseModel):
    tags: list[ResponseTagModel]

    class Config:
        orm_mode = True


class FullResponseTagModel(ResponseTagModel):
    articles: list[ResponseArticleModel]
