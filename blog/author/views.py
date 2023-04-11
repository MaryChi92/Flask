from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.article import views as article_views
from blog.models import Author, User

authors = Blueprint('authors', __name__, url_prefix='/authors', static_folder='../static')


@authors.route('/', endpoint='list')
def authors_list():
    _authors = Author.query.all()
    return render_template('authors/list.html', authors=_authors)
