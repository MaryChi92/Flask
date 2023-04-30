from flask import Flask

from blog import commands
from blog.extensions import db, login_manager, migrate, csrf, admin
from blog.models import User
from blog.article import views as article_views
from blog.auth import views as auth_views
from blog.author import views as author_views
from blog.home import views as home_views
from blog.user import views as user_views
from blog.api import tag, user, author, article


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)
    api.plugins

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog import admin

    app.register_blueprint(user_views.users, url_prefix='/users')
    app.register_blueprint(author_views.authors, url_prefix='/authors')
    app.register_blueprint(article_views.articles, url_prefix='/articles')
    app.register_blueprint(auth_views.auth, url_prefix='/auth')
    app.register_blueprint(home_views.home, url_prefix='/home')

    app.register_blueprint(tag.api_tags, url_prefix='/api/tags')
    app.register_blueprint(user.api_users, url_prefix='/api/users')
    app.register_blueprint(author.api_authors, url_prefix='/api/authors')
    app.register_blueprint(article.api_articles, url_prefix='/api/articles')

    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_tags)
