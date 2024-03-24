from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.api_v1.routes import api

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Development")
    db.init_app(app)
    app.register_blueprint(api)
    app.run()
