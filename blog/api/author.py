from flask import Blueprint
from flask_pydantic import validate
from blog.app import api

from blog.models import Author, User
from blog.schemas import QueryAuthorModel, ResponseAuthorModel, ResponseAuthorsModel


api_authors = Blueprint('api_authors', __name__, url_prefix='/api/authors', static_folder='../static')


@api_authors.route('/', methods=["GET"])
@validate()
def get_authors():
    authors = Author.query.all()
    return ResponseAuthorsModel(
        authors=authors
    )


@api_authors.route('/author')
@validate()
def get_author(query: QueryAuthorModel):
    author_id = query.id
    requested_author = Author.query.filter_by(id=author_id).one_or_none()
    return ResponseAuthorModel(
        id=author_id,
        user=User.query.filter_by(id=requested_author.user_id).one_or_none()
    )
