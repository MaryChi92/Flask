from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.article import views as article_views
from blog.models import User, Article

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


@users.route('/', endpoint='list')
def users_list():
    _users = User.query.all()
    return render_template('users/list.html', users=_users)


@users.route('/<int:pk>', endpoint='details')
@login_required
def user_details(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f"User {pk} doesn't exist!")
    return render_template('users/details.html', user=selected_user)
