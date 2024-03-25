from flask import request,jsonify
from . import api
from .. import db
from ..models import BookingManager,Booking
from .decorators import json, paginate


# Route to create a new booking manager
@api.route('/booking_managers', methods=['POST'])
def create_booking_manager():
    data = request.get_json()
    booking_manager = BookingManager()
    booking_manager.import_data(data)
    db.session.add(booking_manager)
    db.session.commit()
    return jsonify(booking_manager.export_data()), 201

# Route to retrieve all booking managers
@api.route('/booking_managers', methods=['GET'])
def get_all_booking_managers():
    booking_managers = BookingManager.query.all()
    return jsonify([booking_manager.export_data() for booking_manager in booking_managers]), 200

# Route to retrieve a specific booking manager by ID
@api.route('/booking_managers/<int:id>', methods=['GET'])
def get_booking_manager(id):
    booking_manager = BookingManager.query.get_or_404(id)
    return jsonify(booking_manager.export_data()), 200

# Route to update a booking manager by ID
@api.route('/booking_managers/<int:id>', methods=['PUT'])
def update_booking_manager(id):
    booking_manager = BookingManager.query.get_or_404(id)
    data = request.get_json()
    booking_manager.import_data(data)
    db.session.commit()
    return jsonify(booking_manager.export_data()), 200

# Route to delete a booking manager by ID
@api.route('/booking_managers/<int:id>', methods=['DELETE'])
def delete_booking_manager(id):
    booking_manager = BookingManager.query.get_or_404(id)
    db.session.delete(booking_manager)
    db.session.commit()
    return '', 204
