from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

load_dotenv()

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


def create_app():
    from application.settings import (
        initialize_flask_app,
        initialize_plugins,
        import_models,
        register_blueprints
    )
    app = initialize_flask_app()

    with app.app_context():
        # initialize plugins
        initialize_plugins(app)

        # register blueprints
        register_blueprints(app)

        # import models
        import_models()

        return app
