from pydantic import BaseModel
from typing import Optional

from blog.schemas.user import ResponseUserModel


class QueryAuthorModel(BaseModel):
    id: int


class ResponseAuthorModel(BaseModel):

    id: int
    user: Optional[ResponseUserModel]

    class Config:
        orm_mode = True


class ResponseAuthorsModel(BaseModel):
    authors: list[ResponseAuthorModel]
