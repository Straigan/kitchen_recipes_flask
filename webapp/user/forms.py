from flask_wtf import FlaskForm

from webapp.user.models import User

from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Электронный адрес', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "from-check-input"})
    submit = SubmitField('Войти', render_kw={"class": "btn contact-btn"})


class RegistrationForm(FlaskForm):
    email = StringField('Электронный адрес', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    phone_number = StringField('Номер телефона', render_kw={"class": "mask-phone form-control"})
    nick_name = StringField('Ник нейм', render_kw={"class": "form-control"})
    first_name = StringField('Имя', render_kw={"class": "form-control"})
    last_name = StringField('Фамилия', render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')],
                              render_kw={"class": "form-control"})
    submit = SubmitField('Зарегистрироваться', render_kw={"class": "btn contact-btn"})

    def validate_email(self, email: str) -> ValidationError:
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с таким адресом уже существует')

    def validate_phone_number(self, phone_number: str) -> ValidationError:
        if phone_number.data:
            user_count = User.query.filter_by(phone_number=phone_number.data).count()
            if user_count > 0:
                raise ValidationError('Пользователь с таким номером телефона уже существует')
