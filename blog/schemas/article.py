from pydantic import BaseModel
from typing import Optional

from blog.schemas.author import ResponseAuthorModel


class QueryArticleModel(BaseModel):
    id: int


class ResponseArticleModel(BaseModel):

    id: int
    title: str
    body: str
    author: ResponseAuthorModel

    class Config:
        orm_mode = True


class ResponseArticlesModel(BaseModel):
    articles: list[ResponseArticleModel]


class FullResponseArticleModel(ResponseArticleModel):
    from blog.schemas.tag import ResponseTagModel
    tags: list[ResponseTagModel]
