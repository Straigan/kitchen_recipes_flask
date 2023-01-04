from flask import Blueprint, flash, render_template, redirect, url_for, jsonify, session, request, Markup
from flask_login import login_user, logout_user, current_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp.services.service_redirect_utils import redirect_back
from webapp.services.service_empty_field_form import replacing_an_empty_field_with_None
from webapp.user.enums import UserRole


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/sign_in_user')
def sign_in_user():
    if current_user.is_authenticated:
        return redirect_back()

    title = "Sign In"
    form_login = LoginForm()

    return render_template(
        'user/sign_in_user.html',
        title=title,
        form_login=form_login
    )


@blueprint.route('/register_user')
def register_user():
    if current_user.is_authenticated:
        return redirect_back()

    title = "Sign Up"
    form_register = RegistrationForm()

    return render_template(
        'user/register_user.html',
        title=title,
        form_register=form_register,
    )


@blueprint.route('/process_sign_in_user', methods=['POST'])
def process_sign_in_user():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)

            flash("Вы успешно вошли на сайт")
            return redirect(url_for('kitchen_recipes.index'))

        flash('Не правильные имя или пароль')
        return redirect(url_for('user.login_user'))


@blueprint.route('/process_register_user', methods=['POST'])
def process_register_user():
    form = RegistrationForm()

    if form.validate_on_submit():

        new_user = User(
            email=form.email.data,
            phone_number=replacing_an_empty_field_with_None(form.phone_number.data),
            role=UserRole.user,
            nick_name=replacing_an_empty_field_with_None(form.nick_name.data),
            first_name=replacing_an_empty_field_with_None(form.first_name.data),
            last_name=replacing_an_empty_field_with_None(form.last_name.data)
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались и авторизовались')
        login_user(new_user)
        return redirect(url_for('kitchen_recipes.index'))

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Ошибка в поле {}: {}".format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(url_for('user.register_user'))



@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно вышли из сайта')
    return redirect(url_for('kitchen_recipes.index'))