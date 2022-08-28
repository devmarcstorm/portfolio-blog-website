from flask import Flask, redirect, url_for  # pip install Flask
from flask_sqlalchemy import SQLAlchemy  # pip install flask-sqlalchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():

        @app.route("/", methods=["GET"])
        def index():
            return "<h1>Portfolio / Blog</h1>"

        db.create_all()

        return app
