from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

from webapp.kitchen_recipes.views import blueprint as kitchen_recipes_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.db import db
from webapp.kitchen_recipes.models import Category, Recipe
from webapp.user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(kitchen_recipes_blueprint)
    app.register_blueprint(user_blueprint)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    db.init_app(app)
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
        
    return app