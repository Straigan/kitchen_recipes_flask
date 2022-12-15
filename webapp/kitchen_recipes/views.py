from flask import Blueprint, render_template


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