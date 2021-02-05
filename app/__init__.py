from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv
from flask_migrate import Migrate
import flask_praetorian
import flask_cors


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
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()


def create_app():
    from app.settings import (
        register_blueprints,
        initialize_flask_app,
        initialize_plugins,
        initialize_models
    )

    app = initialize_flask_app()

    with app.app_context():

        # register blueprints
        register_blueprints(app)

        # initialize plugins
        initialize_plugins(app)

        # initialize models
        initialize_models()

        # return an flask app instance
        return app
