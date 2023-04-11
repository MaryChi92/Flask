from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import ArticleCreateForm
from blog.models import Article, Author, Tag

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@articles.route('/', endpoint='list', methods=['GET'])
def article_list():
    _articles: Article = Article.query.all()
    return render_template('articles/list.html', articles=_articles)


@articles.route('/<string:tag_name>/', endpoint='filter', methods=['GET'])
def article_list_filtered(tag_name: str):
    _articles: Article = Article.query.options(joinedload(Article.tags)).filter(Article.tags.any(Tag.name == tag_name))
    return render_template('articles/list.html', articles=_articles)


@articles.route('/<int:article_id>/', endpoint='details', methods=['GET'])
def article_details(article_id: int):
    _article: Article = Article.query.filter_by(id=article_id)\
        .options(joinedload(Article.tags))\
        .one_or_none()

    if _article is None:
        raise NotFound(f"Article {article_id} doesn't exist!")
    return render_template('articles/details.html', article=_article)


@articles.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = ArticleCreateForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


@articles.route('/create/', methods=['POST'])
@login_required
def create_article():
    form = ArticleCreateForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), body=form.text.data)

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('articles.details', article_id=_article.id))

    return render_template('articles/create.html', form=form)
