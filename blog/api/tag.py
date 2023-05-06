from flask import Blueprint
from flask_pydantic import validate

from blog.models import Tag
from blog.schemas import QueryTagModel, ResponseTagsModel, FullResponseTagModel


api_tags = Blueprint('api_tags', __name__, url_prefix='/api/tags', static_folder='../static')


@api_tags.route('/', methods=["GET"])
@validate()
def get_tags():
    tags = Tag.query.all()
    return ResponseTagsModel(
        tags=tags
    )


@api_tags.route('/tag')
@validate()
def get_tag(query: QueryTagModel):
    tag_id = query.id
    requested_tag = Tag.query.filter_by(id=tag_id).one_or_none()
    return FullResponseTagModel(
        id=tag_id,
        name=requested_tag.name,
        articles=requested_tag.articles
    )
