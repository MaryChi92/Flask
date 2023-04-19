from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash

from blog.app import db

article_tag_associations_table = Table(
    'article_tag_association',
    db.metadata,
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), nullable=False),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_associations_table, back_populates='articles')


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    articles = relationship('Article', secondary=article_tag_associations_table, back_populates='tags')
