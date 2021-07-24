import os
from os import environ


class Config:
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Static Assets
    STATIC_FOLDER_PATH = environ.get('STATIC_FOLDER_PATH')
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
