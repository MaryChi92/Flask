from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # articles = relationship('Article', back_populates='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password



# class Article(db.Model):
#     __tablename__ = 'articles'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     created_at = db.Column(db.DateTime, default=db.datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=db.datetime.utcnow, onupdate=db.datetime.utcnow)
#
#     user = relationship('User', back_populates='articles')
