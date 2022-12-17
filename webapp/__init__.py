from flask import Flask
from flask_migrate import Migrate

from webapp.kitchen_recipes.views import blueprint as kitchen_recipes_bluprint
from webapp.db import db
from webapp.kitchen_recipes.models import Category, Recipe
from webapp.user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(kitchen_recipes_bluprint)
    db.init_app(app)
    migrate = Migrate(app, db)

    return app