from flask import Flask

from blog.user import views as user_views
from blog.article import views as article_views


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user_views.users, url_prefix='/users')
    app.register_blueprint(article_views.articles, url_prefix='/articles')
