import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(username='test_user', email='test@example.com', password=generate_password_hash('testuser0'), is_staff=True)
        )
        db.session.add(
            User(username='Claire', email='claire@example.com', password=generate_password_hash('claire1'))
        )
        db.session.add(
            User(username='Jensen', email='jensen@example.com', password=generate_password_hash('jensen2'))
        )
        db.session.commit()

@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('travel', 'restaurant', 'review', 'advice', 'lifestyle', 'hotel')
        for tag in tags:
            db.session.add(Tag(name=tag))
        db.session.commit()
