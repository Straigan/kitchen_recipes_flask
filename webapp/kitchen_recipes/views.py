from flask import Blueprint, flash, render_template, redirect, url_for

from webapp.kitchen_recipes.forms import AddNewRecipeForm
from webapp.kitchen_recipes.models import Recipe
from webapp.db import db


blueprint = Blueprint('kitchen_recipes', __name__)

@blueprint.route('/')
def index():
    title = "Главная страница"
    context = "Рецепты"
    return render_template(
        'kitchen_recipes/index.html',
        title=title,
        context=context,
    )


@blueprint.route('/add_recipe')
def add_recipe():
    title = 'Добавление рецепта'
    form = AddNewRecipeForm()
    return render_template(
        'kitchen_recipes/add_recipe.html',
        title=title,
        form=form
    )


@blueprint.route('/process_add_recipe', methods=['POST'])
def process_add_recipe():
    form = AddNewRecipeForm()
    if form.validate_on_submit():
        new_recipe = Recipe(
            category_id = form.category.data,
            name = form.name.data,
            description = form.description.data,
        )
    
        db.session.add(new_recipe)
        db.session.commit()
    
        flash('Вы добавили рецепт')
        return redirect(url_for('kitchen_recipes.index'))
    else:
        for field, error in form.errors.items():
            flash('Ошибка в поле {}: {}'.format(
                getattr(form, field).lavel.text,
                error
            ))
    return redirect(url_for('kitchen_recipes.add_recipe'))