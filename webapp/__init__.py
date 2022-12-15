from flask import Flask

from webapp.kitchen_recipes.views import blueprint as kitchen_recipes_bluprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(kitchen_recipes_bluprint)

    return app