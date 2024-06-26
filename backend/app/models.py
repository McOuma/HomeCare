"""
Module defining database models for the application.
"""

# Standard library imports
from datetime import datetime, timedelta

import jwt

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# Third-party imports
from flask import current_app, url_for
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

# Local application imports
from app import db, login_manager
from app.exceptions import ValidationError


class User(db.Model, UserMixin):
    """Model representing a user in the system."""

    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    # token = db.Column(db.String(128))
    # role = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    # Define a relationship with Caregiver
    caregiver = relationship("Caregiver", backref="user", uselist=False)
    # Define a relationship with Client
    client = relationship("Client", backref="user", uselist=False)

    # Define a relationship with Booking
    bookings = relationship("Booking", backref="user", lazy="dynamic")

    def set_password(self, password):
        """Set the password for the user."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Verify the user's password."""
        return check_password_hash(self.password_hash, password)

    def generate_token(self, expiration=3600):
        payload = {
            "id": self.id,
            "exp": datetime.utcnow() + timedelta(seconds=expiration),
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        return token.decode("utf-8")

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            return payload["id"]
        except jwt.ExpiredSignatureError:
            # Token has expired
            return None
        except jwt.InvalidTokenError:
            # Token is invalid
            return None

    # def generate_token(self):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
    #     self.token = s.dumps({'id': self.id}).decode('utf-8')
    #     return self.token

    # @classmethod
    # def verify_token(cls, token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)
    #     except:
    #         return None
    #     return User.query.get(data['id'])

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Caregiver(db.Model):
    """Model representing a caregiver in the system."""

    __tablename__ = "caregiver"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    contact = db.Column(db.Integer(), nullable=False)
    national_id = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    bookings = db.relationship("Booking", backref="caregiver", lazy="dynamic")

    def get_url(self):
        """Get the URL for accessing the caregiver's information."""
        return url_for("api.get_caregiver", id=self.id, _external=True)

    def export_data(self):
        """Export data of the caregiver in a dictionary format."""
        return {
            "self_url": self.get_url(),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "location": self.location,
            "contact": self.contact,
            "national_id": self.national_id,
            "created_on": self.created_on.isoformat(),
        }

    def import_data(self, data):
        """Import data to update the caregiver's information."""
        try:
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]
            self.location = data["location"]
            self.contact = data["contact"]
            self.national_id = data["national_id"]
        except KeyError as e:
            raise ValidationError("Invalid caregiver data: missing " + e.args[0]) from e
        return self


class Client(db.Model):
    """Model representing clients in the system."""

    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    contact = db.Column(db.Integer(), nullable=False)
    national_id = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationship to bookings
    bookings = db.relationship("Booking", backref="client", lazy="dynamic")

    def get_url(self):
        """Get the URL for accessing the client's information."""
        return url_for("api.get_client", id=self.id, _external=True)

    def export_data(self):
        """Export data of the client in a dictionary format."""
        return {
            "self_url": self.get_url(),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "location": self.location,
            "contact": self.contact,
            "national_id": self.national_id,
            "created_on": self.created_on.isoformat(),
        }

    def import_data(self, data):
        """Import data to update the client's information."""
        try:
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]
            self.location = data["location"]
            self.contact = data["contact"]
            self.national_id = data["national_id"]
        except KeyError as e:
            raise ValidationError("Invalid client data: missing " + e.args[0]) from e
        return self


class Service(db.Model):
    """Model representing service entities in the system."""

    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(), nullable=False)
    service_price = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def get_url(self):
        """Get the URL for accessing the service's information."""
        return url_for("api.get_service", id=self.id, _external=True)

    def export_data(self):
        """Export data of the service in a dictionary format."""
        return {
            "self_url": self.get_url(),
            "service_type": self.service_type,
            "service_price": self.service_price,
            "description": self.description,
            "created_on": self.created_on.isoformat(),
        }

    def import_data(self, data):
        """Import data to update the service's information."""
        try:
            self.service_type = data["service_type"]
            self.service_price = data["service_price"]
            self.description = data["description"]
        except KeyError as e:
            raise ValidationError("Invalid service data: missing " + e.args[0]) from e
        return self


class Booking(db.Model):
    """Model representing booking entities in the system."""

    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    caregiver_id = db.Column(db.Integer, db.ForeignKey("caregiver.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    # Adjust the relationship to users
    # Correct the backref in the Booking model
    user_relation = relationship(
        "User", back_populates="bookings", overlaps="booking,user"
    )

    def get_url(self):
        """Get the URL for accessing the booking's information."""
        return url_for("api.get_booking", id=self.id, _external=True)

    def export_data(self):
        """Export data of the booking in a dictionary format."""
        return {
            "self_url": self.get_url(),
            "client_id": self.client_id,
            "service_id": self.service_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "status": self.status,
        }

    def import_data(self, data):
        """Import data to update the booking's information."""
        try:
            self.client_id = data["client_id"]
            self.service_id = data["service_id"]
            self.start_date = datetime.fromisoformat(data["start_date"])
            self.end_date = datetime.fromisoformat(data["end_date"])
            self.status = data["status"]
        except KeyError as e:
            raise ValidationError("Invalid booking data: missing " + e.args[0]) from e
        return self

    @property
    def duration(self):
        """Calculate the duration of the booking."""
        return (self.end_date - self.start_date).days


class BookingManager(db.Model):
    """Model representing booking manager entities in the system."""

    __tablename__ = "booking_manager"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    client = relationship("Client", backref="booking_manager")
    service = relationship("Service", backref="booking_manager")

    def get_url(self):
        """Get the URL for accessing the booking manager's information."""
        return url_for("api.get_booking_manager", id=self.id, _external=True)

    def export_data(self):
        """Export data of the booking manager in a dictionary format."""
        return {
            "self_url": self.get_url(),
            "client_id": self.client_id,
            "service_id": self.service_id,
            "booking_date": self.booking_date.isoformat(),
            "status": self.status,
        }

    def import_data(self, data):
        """Import data to update the booking manager's information."""
        try:
            self.client_id = data["client_id"]
            self.service_id = data["service_id"]
            self.booking_date = datetime.fromisoformat(data["booking_date"])
            self.status = data["status"]
        except KeyError as e:
            raise ValidationError("Invalid booking data: missing " + e.args[0]) from e
        return self


class Review(db.Model):
    """Model representing reviews in the system."""

    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"))
    comment = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    client = relationship("Client", backref="review")
    service = relationship("Service", backref="review")
    booking = relationship("Booking", backref="review")

    def get_url(self):
        """Get the URL for accessing the review's information."""
        return url_for("api.get_review", id=self.id, _external=True)

    def export_data(self):
        """Export data of the review in a dictionary format."""
        return {
            "self_url": self.get_url(),
            "rating": self.rating,
            "comment": self.comment,
            "client_url": url_for("api.get_client", id=self.client_id, _external=True),
            "service_url": url_for(
                "api.get_service", id=self.service_id, _external=True
            ),
            "booking_url": url_for(
                "api.get_booking", id=self.booking_id, _external=True
            ),
        }

    def import_data(self, data):
        """Import data to update the review's information."""
        try:
            self.comment = data["comment"]
            self.rating = data["rating"]
            self.client_id = data["client_id"]
            self.service_id = data["service_id"]
            self.booking_id = data["booking_id"]
        except KeyError as e:
            raise ValidationError("Invalid review data: missing " + e.args[0]) from e
        return self

    def calculate_average_rating(self):
        """
        Calculate the average rating of all reviews for a specific service.
        """
        total_rating = sum(review.rating for review in self.service.reviews)
        total_reviews = self.service.reviews.count()
        return total_rating / total_reviews if total_reviews else 0

    def get_client_name(self):
        """
        Get the full name of the client who made the review.
        """
        return f"{self.client.first_name} {self.client.last_name}"
