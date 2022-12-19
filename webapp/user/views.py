from flask import Blueprint, flash, render_template, redirect, url_for, jsonify, session, request, Markup
from flask_login import current_user, login_user, logout_user, login_required

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login_register')
def login_or_register_user():
    if current_user.is_authenticated:
        return redirect('users/login_register')

    title_login = "Sign In"
    form_login = LoginForm()

    title_register = "Sign Up"
    form_register = RegistrationForm()

    return render_template(
        'user/login_register.html',
        title_login=title_login,
        title_register=title_register,
        form_login=form_login,
        form_register=form_register,
    )