from loguru import logger

import pandas

from sqlalchemy import exc

from webapp import create_app
from webapp.db import db
from webapp.kitchen_recipes.models import Category, Photo, Recipe
from webapp.user.models import User


def dataframe_from_excel(data) -> pandas.DataFrame:
    columns_name = ['category_name', 'recipe_name', 'description', 'photo_path']
    products_frame = pandas.DataFrame(data, columns=columns_name)

    return products_frame


def copy_category_in_db(dataset):
    categories = dataset['category_name'].unique()
    for category in categories:
        category_in_db = Category.query.filter(Category.name == category).first()
        if category == '':
            continue
        elif category_in_db:
            if category == category_in_db.name:
                continue
        else:
            new_category = Category(name=category)
            db.session.add(new_category)
    db.session.commit()
    logger.info("Категории скопированы из excel в DB")


def copy_recipe_in_db(dataset):
    categories = Category.query.all()
    user_role_admin = User.query.filter_by(role='admin').first()
    dict_id_categories = {category.name: category.id for category in categories}
    try:
        for _, row in dataset.iterrows():
            recipe = Recipe.query.filter(Recipe.name == row['recipe_name']).first()
            if row['recipe_name'] == '' or row['description'] == '':
                continue
            elif recipe:
                if row['recipe_name'] == recipe.name:
                    continue
            elif row['category_name'] in dict_id_categories:
                new_recipe = Recipe(
                    name=row['recipe_name'],
                    description=row['description'],
                    category_id=dict_id_categories[row['category_name']],
                    user_id=user_role_admin.id,
                )
                db.session.add(new_recipe)
    except exc.SQLAlchemyError:
        return logger.error('''Отсуствуют не обоходимые данные для колонок:
                        название рецепта, описание, категория или пользователь с ролью админ''')
    db.session.commit()
    logger.info("Рецепты скопированы из excel в DB")


def copy_images_in_db(dataset):
    recipes = Recipe.query.all()
    dist_id_recipes = {recipe.name: recipe.id for recipe in recipes}
    for _, row in dataset.iterrows():
        photo_path_in_db = Photo.query.filter(Photo.photo_path == row['photo_path']).first()
        if row['photo_path'] == '':
            continue
        elif photo_path_in_db:
            if row['photo_path'] == photo_path_in_db.photo_path:
                continue
        else:
            new_image = Photo(
                recipe_id=dist_id_recipes[row['recipe_name']],
                photo_path=row['photo_path'],
            )
            db.session.add(new_image)
    db.session.commit()
    logger.info("Пути к картинкам рецептов скопированы из excel в DB")


if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        data = pandas.read_excel('recipe.xlsx', na_filter=False)
        categories_recipies_dataframe = dataframe_from_excel(data)
        copy_category_in_db(data)
        copy_recipe_in_db(categories_recipies_dataframe)
        copy_images_in_db(categories_recipies_dataframe)
