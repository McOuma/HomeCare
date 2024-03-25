from flask import request,jsonify
from . import api
from .. import db
from ..models import Review,Service
from .decorators import json, paginate


# Review Routes
@api.route("/reviews/", methods=["POST"])
def create_review():
    """
    Create a new review.
    """
    data = request.json
    review = Review()
    review.import_data(data)
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review created successfully.", "review_id": review.id}), 201


@api.route("/reviews/<int:review_id>/", methods=["GET"])
def get_review(review_id):
    """
    Retrieve a specific review by its ID.
    """
    review = Review.query.get_or_404(review_id)
    return jsonify(review.export_data())


@api.route("/reviews/<int:review_id>/", methods=["PUT"])
def update_review(review_id):
    """
    Update an existing review by its ID.
    """
    review = Review.query.get_or_404(review_id)
    data = request.json
    review.import_data(data)
    db.session.commit()
    return jsonify({"message": "Review updated successfully."})



@api.route("/reviews/<int:review_id>/", methods=["DELETE"])
def delete_review(review_id):
    """
    Delete a review by its ID.
    """
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully."})



@api.route("/reviews/<int:review_id>/average_rating/", methods=["GET"])
def get_review_average_rating(review_id):
    """
    Retrieve the average rating for a specific review.
    """
    review = Review.query.get_or_404(review_id)
    average_rating = review.calculate_average_rating()
    return jsonify({"average_rating": average_rating})



@api.route("/reviews/<int:review_id>/client_name/", methods=["GET"])
def get_review_client_name(review_id):
    """
    Retrieve the full name of the client who made the review.
    """
    review = Review.query.get_or_404(review_id)
    client_name = review.get_client_name()
    return jsonify({"client_name": client_name})



@api.route("/services/<int:service_id>/average_rating/", methods=["GET"])
def get_service_average_rating(service_id):
    """
    Retrieve the average rating for a specific service.
    """
    service = Service.query.get_or_404(service_id)
    average_rating = service.calculate_average_rating()
    return jsonify({"average_rating": average_rating})
