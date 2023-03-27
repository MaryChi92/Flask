from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.article import views as article_views

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: "Claire",
    2: "Colin",
    3: "Jensen",
}


@users.route('/', endpoint='list')
def users_list():
    return render_template('users/list.html', users=USERS)


@users.route('/<int:user_id>', endpoint='details')
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
        articles = article_views.ARTICLES
    except KeyError:
        raise NotFound(f"User {user_id} doesn't exist!")
    return render_template('users/details.html', user_id=user_id, user_name=user_name, articles=articles)
