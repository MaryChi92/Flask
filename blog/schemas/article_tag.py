from pydantic import BaseModel
# from blog.schemas.article import ResponseArticleModel
from blog.schemas.author import ResponseAuthorModel


class Headers(BaseModel):
    authorization: str


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


class FullResponseTagModel(ResponseTagModel):
    articles: list[ResponseArticleModel]


class FullResponseArticleModel(ResponseArticleModel):
    tags: list[ResponseTagModel]
