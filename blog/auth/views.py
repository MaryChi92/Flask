from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('User with this email already exists')
            return render_template('auth/register.html', form=form)

        _user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)

    return render_template('auth/register.html', form=form, errors=errors)


@auth.route('/login', methods=['GET'])
def login():
    form = UserLoginForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template('auth/login.html', form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    form = UserLoginForm(request.form)
    errors = []

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            errors.append('Check login credentials please!')
            return render_template('auth/register.html', form=form)

        login_user(user)
        return redirect(url_for('users.details', pk=user.id))

    return render_template('auth/register.html', form=form, errors=errors)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
