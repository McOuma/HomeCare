from flask import request,jsonify
from . import api
from .. import db
from ..models import Caregiver,Review,Client
from .decorators import json, paginate



@api.route("/caregivers/", methods=["GET"])
@paginate("bookings")
def get_caregiver():
    return Caregiver.query


@api.route("/caregivers/<int:id>", methods=["GET"])
@json
def get_caregiver_by_id(id):
    return Caregiver.query.get_or_404(id)


@api.route('/caregivers/', methods=['POST'])
@json
def new_caregiver():
    new_caregiver = Caregiver()
    new_caregiver.import_data(request.json)
    db.session.add(new_caregiver)
    db.session.commit()
    return {}, 201, {'Location': new_caregiver.get_url()}


@api.route('/caregivers/<int:id>/', methods=['PUT'])
@json
def edit_caregiver_details(id):
    caregiver = Caregiver.query.get_or_404(id)
    caregiver.import_data(request.json)
    db.session.add(caregiver)
    db.session.commit()
    return {}


# Caregiver Review Routes
@api.route("/caregivers/<int:caregiver_id>/reviews/", methods=["POST"])
def create_caregiver_review(caregiver_id):
    data = request.json
    client_id = data.get("client_id")
    rating = data.get("rating")
    comment = data.get("comment")
    if not all([client_id, rating]):
        return jsonify({"error": "Client ID and rating are required."}), 400
    caregiver = Caregiver.query.get_or_404(caregiver_id)
    client = Client.query.get_or_404(client_id)
    review = Review(client_id=client_id, caregiver_id=caregiver_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review created successfully.", "review_id": review.id}), 201



@api.route("/caregivers/<int:caregiver_id>/reviews/", methods=["GET"])
def get_caregiver_reviews(caregiver_id):
    """
    Retrieve all reviews made by the caregiver (identified by ID).
    """
    caregiver = Caregiver.query.get_or_404(caregiver_id)
    reviews = Review.query.filter_by(caregiver_id=caregiver_id).all()
    return jsonify([review.export_data() for review in reviews])



@api.route("/caregivers/<int:caregiver_id>/reviews/<int:review_id>/", methods=["GET"])
def get_caregiver_review(caregiver_id, review_id):
    """
    Retrieve a specific review made by the caregiver (identified by ID).
    """
    review = Review.query.filter_by(caregiver_id=caregiver_id, id=review_id).first_or_404()
    return jsonify(review.export_data())



@api.route("/caregivers/<int:caregiver_id>/reviews/<int:review_id>/", methods=["PUT"])
def update_caregiver_review(caregiver_id, review_id):
    """
    Update a review made by the caregiver (identified by ID).
    """
    review = Review.query.filter_by(caregiver_id=caregiver_id, id=review_id).first_or_404()
    data = request.json
    if 'rating' in data:
        review.rating = data['rating']
    if 'comment' in data:
        review.comment = data['comment']
    db.session.commit()
    return jsonify({"message": "Review updated successfully."})


@api.route("/caregivers/<int:caregiver_id>/reviews/<int:review_id>/", methods=["DELETE"])
def delete_caregiver_review(caregiver_id, review_id):
    """
    Delete a review made by the caregiver (identified by ID).
    """
    review = Review.query.filter_by(caregiver_id=caregiver_id, id=review_id).first_or_404()
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully."})
