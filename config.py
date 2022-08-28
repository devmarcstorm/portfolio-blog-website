from os import environ, path

from dotenv import load_dotenv  # pip install python-dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    BASE_DIR = BASE_DIR

    # General
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_RUN_HOST = environ.get("FLASK_RUN_HOST")

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Uploads
    UPLOAD_SUBMISSION_KEY = environ.get("UPLOAD_SUBMISSION_KEY")
    MAX_UNAUTHORIZED_REQUESTS_BEFORE_BAN = int(
        environ.get("MAX_UNAUTHORIZED_REQUESTS_BEFORE_BAN")
    )

    # Logs
    LOGS_DIRECTORY = environ.get("LOGS_DIRECTORY")
