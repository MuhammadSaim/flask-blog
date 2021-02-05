from flask import Flask

from app import (
    db,
    migrate,
    guard,
    cors
)

from app.models.user import User


def register_blueprints(app):
    from app.controllers import (
        home,
        auth
    )
    app.register_blueprint(home.controller)
    app.register_blueprint(auth.controller)


def initialize_plugins(app):
    db.init_app(app)
    migrate.init_app(app, db)
    guard.init_app(app, User)
    cors.init_app(app)


def initialize_models():
    # Import Database Models
    from app.models import (
        user,
        post
    )


def initialize_flask_app():
    # initialize the core flask app
    from config import Config
    app = Flask(__name__,
                instance_relative_config=False,
                template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object('config.Config')
    return app
