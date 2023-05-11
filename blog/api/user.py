from flask import Blueprint
from flask_pydantic import validate

from blog.models import User
from blog.schemas import QueryUserModel, ResponseUserModel, ResponseUsersModel


api_users = Blueprint('api_users', __name__, url_prefix='/api/users', static_folder='../static')


@api_users.route('/', methods=["GET"])
@validate()
def get_users():
    users = User.query.all()
    return ResponseUsersModel(
        users=users
    )


@api_users.route('/user')
@validate()
def get_user(query: QueryUserModel):
    user_id = query.id
    requested_user = User.query.filter_by(id=user_id).one_or_none()
    return ResponseUserModel(
        id=user_id,
        username=requested_user.username,
        email=requested_user.email
    )
