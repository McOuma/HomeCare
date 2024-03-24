from app import db
from flask import url_for
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash



class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    @hybrid_property
    def get_password(self):
        return self.password_hash

    @password_hash.setter
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Caregiver(User):
    id  = db.Column(db.Integer(), foreign_key = True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    contact = db.Column(db.Integer(), nullable=False)
    national_id = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


class Client(User):
    id  = db.Column(db.Integer(), foreign_key = True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    contact = db.Column(db.Integer(), nullable=False)
    national_id = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


class Service(db.Model):
    id  = db.Column(db.Integer(), foreign_key = True)
    service_type = db.Column(db.String(), nullable=False)
    service_price = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    duration = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


class Booking(db.Model):
    id  = db.Column(db.Integer(), foreign_key = True)
    client_name = db.Column(db.String(), nullable=False)
    service = db.Column(db.String(), nullable=False)
    booking_date = db.Column(db.String(), nullable=False)
    status = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)



class Booking_manager(db.Model):
    id  = db.Column(db.Integer(), foreign_key = True)
    client_name = db.Column(db.String(), nullable=False)
    service_name = db.Column(db.String(), nullable=False)
    booking_date = db.Column(db.String(), nullable=False)
    status = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


class Review(db.Model):
    id  = db.Column(db.Integer(), primary_key = True)
    client_id = db.Column(db.Integer(), foreign_key=True)
    service_id = db.Column(db.Integer(), foreign_key=True)
    booking_id = db.Column(db.Integer(), foreign_key=True)
    comment = db.Column(db.String(), nullable=False)
    rating = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def get_url(self):
        return url_for('api.get_review', id=self.id, _external=True)



    def export_data(self):
        return {
            'self_url': self.get_url(),
            'rating': self.rating,
             'comment': self.comment,
            'client_url': url_for('api.get_client', id=self.id,
                                  _external=True)
        }
