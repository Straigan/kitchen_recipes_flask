from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user

from webapp.kitchen_recipes.forms import AddNewRecipeForm
from webapp.kitchen_recipes.models import Recipe
from webapp.db import db


blueprint = Blueprint('kitchen_recipes', __name__)

@blueprint.route('/')
def index():
    title = "Главная страница"
    context = "Рецепты"
    recipes = Recipe.query.all()
    return render_template(
        'kitchen_recipes/index.html',
        title=title,
        context=context,
        recipes=recipes
    )


# @blueprint.route('/<int:recipe_id>')
# def page_recipe(recipe_id):



@blueprint.route('/add_recipe')
def add_recipe():
    title = 'Добавление рецепта'
    form_add_recipe = AddNewRecipeForm()
    return render_template(
        'kitchen_recipes/add_recipe.html',
        title=title,
        form_add_recipe=form_add_recipe
    )


@blueprint.route('/process_add_recipe', methods=['POST'])
def process_add_recipe():
    form = AddNewRecipeForm()
    if form.validate_on_submit():
        new_recipe = Recipe(
            category_id = form.category.data,
            user_id=current_user.id,
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


@blueprint.route('/delete_recipe/<int:recipe_id>')
def process_delete_recipe(recipe_id):
    if not current_user.is_authenticated:
        return redirect(url_for('kitchen_recipes.index'))
    else:
        delete_recipe = Recipe.query.filter(Recipe.user_id == current_user.user_id,
                                            Recipe.id == recipe_id
                                    ).delete()
        db.session.commit()
        flash('Вы успешно удалили рецепт')
        return redirect(url_for('kitchen_recipes.index'))