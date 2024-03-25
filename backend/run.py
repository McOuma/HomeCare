#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User
# from flask_migrate import Migrate, upgrade

# # Initialize Flask-Migrate
# migrate = Migrate()

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

    # # Initialize Flask-Migrate with the app and the database instance
    # migrate.init_app(app, db)

    # # Register Flask-Migrate commands
    # @app.cli.command()
    # def db_init():
    #     """Alias for 'flask db init'."""
    #     pass

    # @app.cli.command()
    # def db_migrate():
    #     """Alias for 'flask db migrate'."""
    #     pass

    # @app.cli.command()
    # def db_upgrade():
    #     """Alias for 'flask db upgrade'."""
    #     upgrade()

    # Use app.app_context() to work with the application within the context
    with app.app_context():
        # # Perform any database migrations
        # upgrade()

        # Create database tables if they don't exist
        db.create_all()

        # Create a development user
        if db.session.query(User).filter_by(id=1).first() is None:
            u = User(username='muga', email='oumamugah@gmail.com')
            u.set_password('salting')
            db.session.add(u)
            db.session.commit()

    # Run the Flask application
    app.run()
