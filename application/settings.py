from flask import Flask
import os

import config
from application import (
    db,
    migrate,
    toolbar
)


def register_blueprints(app):
    from application.controllers import (
        home
    )

    app.register_blueprint(home.controller)


def initialize_plugins(app):
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)


def import_models():
    # import database models
    from application.models import (
        user
    )


def initialize_flask_app():
    # Initialize the core application.
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder=config.Config.TEMPLATES_FOLDER,
        static_folder=config.Config.STATIC_FOLDER,
        static_url_path=config.Config.STATIC_FOLDER_PATH
    )
    app.config.from_object('config.Config')
    return app
