#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User


if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

    with app.app_context():

        db.create_all()

        # Create a development user
        if db.session.query(User).filter_by(id=1).first() is None:
            u = User(username='liam', email='liam@gmail.com')
            u.set_password('dog')
            db.session.add(u)
            db.session.commit()


    app.run()
