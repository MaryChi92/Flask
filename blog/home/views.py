from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/home', static_folder='../static')


@home.route('/')
def homepage():
    return render_template('index.html')
