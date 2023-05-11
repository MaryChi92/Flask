from flask import Blueprint
from flask_pydantic import validate

from blog.models import Article, Author
from blog.schemas import QueryArticleModel, ResponseArticlesModel, FullResponseArticleModel


api_articles = Blueprint('api_articles', __name__, url_prefix='/api/articles', static_folder='../static')


@api_articles.route('/', methods=["GET"])
@validate()
def get_articles():
    articles = Article.query.all()
    return ResponseArticlesModel(
        articles=articles
    )


@api_articles.route('/article')
@validate()
def get_article(query: QueryArticleModel):
    article_id = query.id
    requested_article = Article.query.filter_by(id=article_id).one_or_none()
    return FullResponseArticleModel(
        id=article_id,
        title=requested_article.title,
        body=requested_article.body,
        author=Author.query.filter_by(id=requested_article.author_id).one_or_none(),
        tags=requested_article.tags
    )
