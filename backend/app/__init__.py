#!/usr/bin/env python
import os
from flask import Flask,g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

    # Apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # Initialize extensions
    db.init_app(app)

    login_manager.init_app(app)

    # Register blueprints
    from app.api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # Register an after request handler
    @app.after_request
    def after_request(rv):
        headers = getattr(g, 'headers', {})
        rv.headers.extend(headers)
        return rv


    # Authentication token route
    from app.auth import auth
    from app.api_v1.decorators import rate_limit, json, no_cache
    @app.route('/get-auth-token')
    @auth.login_required
    @rate_limit(limit=1, period=600)  # one call per 10 minute period
    @no_cache
    @json
    def get_auth_token():
        return {'token': g.user.generate_auth_token()}

    return app
