from datetime import datetime

from flask_wtf import FlaskForm

from webapp.kitchen_recipes.models import Category

from wtforms import DateTimeField, FileField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddNewRecipeForm(FlaskForm):
    category = SelectField('Вид блюда', coerce=int, choices=[], validators=[DataRequired()])
    name = StringField('Название продукта', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = TextAreaField('Ингредиенты', render_kw={"class": "form-control"})
    photo = FileField('Добавить фото', validators=[DataRequired()])
    submit = SubmitField('Отправить!', render_kw={"class": "btn contact-btn"})
    create_at = DateTimeField('Дата создания', default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(AddNewRecipeForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) for category in Category.query.all()]
