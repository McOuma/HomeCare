#!/usr/bin/env python
import logging
import os

from flask import Flask, g
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

    # Apply configuration
    cfg = os.path.join(os.getcwd(), "config", config_name + ".py")
    app.config.from_pyfile(cfg)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Set up logging
    # log_level = app.config.get("LOG_LEVEL", "INFO")
    # log_file = app.config.get("LOG_FILE", "app.log")
    # logging.basicConfig(filename=log_file, level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Register blueprints
    from app.api_v1 import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    # Register an after request handler
    @app.after_request
    def after_request(rv):
        headers = getattr(g, "headers", {})
        rv.headers.extend(headers)
        return rv

    # Authentication token route
    from app.api_v1.decorators import json, no_cache, rate_limit
    from app.auth import auth

    @app.route("/get-auth-token")
    @auth.login_required
    @rate_limit(limit=1, period=600)  # one call per 10 minute period
    @no_cache
    @json
    def get_auth_token():
        return {"token": g.user.generate_auth_token()}

    return app
