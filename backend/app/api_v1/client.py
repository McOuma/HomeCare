from datetime import datetime, timedelta

from flask import jsonify, request

from .. import db
from ..models import Booking, BookingManager, Caregiver, Client, Review
from . import api
from .decorators import json, paginate


# Route to create a new client
@api.route("/clients/", methods=["POST"])
def create_client():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided."}), 400
    client = Client()
    client.import_data(data)
    db.session.add(client)
    db.session.commit()
    return (
        jsonify({"message": "Client created successfully.", "client_id": client.id}),
        201,
    )


# Route to retrieve all clients
@api.route("/clients/", methods=["GET"])
def get_clients():
    clients = Client.query.all()
    client_data = [client.export_data() for client in clients]
    return jsonify({"clients": client_data}), 200


# Route to retrieve a specific client by ID
@api.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify(client.export_data()), 200


# Route to update a client's information
@api.route("/clients/<int:client_id>/", methods=["PUT"])
def update_client(client_id):
    client = Client.query.get_or_404(client_id)
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided."}), 400
    client.import_data(data)
    db.session.commit()
    return jsonify({"message": "Client updated successfully."}), 200


# Route to delete a client
@api.route("/clients/<int:client_id>/", methods=["DELETE"])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({"message": "Client deleted successfully."}), 200


# Route to create a new booking for a client
@api.route("/clients/<int:client_id>/bookings/", methods=["POST"])
def create_booking(client_id):
    client = Client.query.get_or_404(client_id)
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided."}), 400
    booking = Booking(client_id=client_id)
    booking.import_data(data)
    db.session.add(booking)
    db.session.commit()
    return (
        jsonify({"message": "Booking created successfully.", "booking_id": booking.id}),
        201,
    )


# Route to retrieve bookings associated with a client
@api.route("/clients/<int:client_id>/bookings/", methods=["GET"])
def get_client_bookings(client_id):
    client = Client.query.get_or_404(client_id)
    bookings = client.bookings.all()
    booking_data = [booking.export_data() for booking in bookings]
    return jsonify({"bookings": booking_data}), 200


# Route to interact with booking manager for a client
@api.route("/clients/<int:client_id>/booking_manager/", methods=["GET", "POST"])
def client_booking_manager(client_id):
    if request.method == "GET":
        booking_manager = BookingManager.query.filter_by(client_id=client_id).first()
        if booking_manager:
            booking_manager_data = booking_manager.export_data()
            return jsonify(booking_manager_data), 200
        else:
            return (
                jsonify({"message": "Booking manager not found for this client."}),
                404,
            )
    elif request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"message": "No data provided."}), 400
        booking_manager = BookingManager.query.filter_by(client_id=client_id).first()
        if booking_manager:
            booking_manager.import_data(data)
        else:
            booking_manager = BookingManager(client_id=client_id)
            booking_manager.import_data(data)
            db.session.add(booking_manager)
        db.session.commit()
        return jsonify({"message": "Booking manager updated successfully."}), 200

    # Client Review Routes


@api.route("/clients/<int:client_id>/reviews/", methods=["POST"])
def create_client_review(client_id):
    """
    Create a review for a client (identified by ID).
    """
    data = request.json
    caregiver_id = data.get("caregiver_id")
    rating = data.get("rating")
    comment = data.get("comment")
    if not all([caregiver_id, rating]):
        return jsonify({"error": "Caregiver ID and rating are required."}), 400
    client = Client.query.get_or_404(client_id)
    caregiver = Caregiver.query.get_or_404(caregiver_id)
    review = Review(
        client_id=client_id, caregiver_id=caregiver_id, rating=rating, comment=comment
    )
    db.session.add(review)
    db.session.commit()
    return (
        jsonify({"message": "Review created successfully.", "review_id": review.id}),
        201,
    )


@api.route("/clients/<int:client_id>/reviews/", methods=["GET"])
def get_client_reviews(client_id):
    """
    Retrieve all reviews made by the client (identified by ID).
    """
    client = Client.query.get_or_404(client_id)
    reviews = Review.query.filter_by(client_id=client_id).all()
    return jsonify([review.export_data() for review in reviews])


@api.route("/clients/<int:client_id>/reviews/<int:review_id>/", methods=["GET"])
def get_client_review(client_id, review_id):
    """
    Retrieve a specific review made by the client (identified by ID).
    """
    review = Review.query.filter_by(client_id=client_id, id=review_id).first_or_404()
    return jsonify(review.export_data())


@api.route("/clients/<int:client_id>/reviews/<int:review_id>/", methods=["PUT"])
def update_client_review(client_id, review_id):
    """
    Update a review made by the client (identified by ID).
    """
    review = Review.query.filter_by(client_id=client_id, id=review_id).first_or_404()
    data = request.json
    if "rating" in data:
        review.rating = data["rating"]
    if "comment" in data:
        review.comment = data["comment"]
    db.session.commit()
    return jsonify({"message": "Review updated successfully."})


@api.route("/clients/<int:client_id>/reviews/<int:review_id>/", methods=["DELETE"])
def delete_client_review(client_id, review_id):
    """
    Delete a review made by the client (identified by ID).
    """
    review = Review.query.filter_by(client_id=client_id, id=review_id).first_or_404()
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully."})
