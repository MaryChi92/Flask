from flask import Flask

from blog import commands
from blog.extensions import db, login_manager, migrate
from blog.models import User
from blog.article import views as article_views
from blog.user import views as user_views
from blog.auth import views as auth_views


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

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    app.register_blueprint(user_views.users, url_prefix='/users')
    app.register_blueprint(article_views.articles, url_prefix='/articles')
    app.register_blueprint(auth_views.auth, url_prefix='/login')


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
