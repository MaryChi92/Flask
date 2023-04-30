from pydantic import BaseModel
from typing import Optional

from blog.schemas.author import ResponseAuthorModel
from blog.schemas.tag import ResponseTagsModel


class QueryArticleModel(BaseModel):
    id: int


class ResponseArticleModel(BaseModel):

    id: int
    title: str
    body: str
    author: ResponseAuthorModel
    # tags: Optional[ResponseTagsModel]

    class Config:
        orm_mode = True


class ResponseArticlesModel(BaseModel):
    articles: list[ResponseArticleModel]
