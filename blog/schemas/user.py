from pydantic import BaseModel, EmailStr


class QueryUserModel(BaseModel):
    id: int


class ResponseUserModel(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class ResponseUsersModel(BaseModel):
    users: list[ResponseUserModel]
