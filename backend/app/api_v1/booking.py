from flask import request,jsonify
from . import api
from .. import db
from ..models import Booking,BookingManager,Caregiver
from .decorators import json, paginate
from datetime import datetime, timedelta

@api.route("/bookings/", methods=["GET"])
def get_bookings():
    return Booking.query


@api.route("/bookings/<int:id>", methods=["GET"])
@json
def get_booking_by_id(id):
    return Booking.query.get_or_404(id)


@api.route('/bookings/', methods=['POST'])
@json
def new_booking():
    booking = Booking()
    booking.import_data(request.json)
    db.session.add(booking)
    db.session.commit()
    return {}, 201, {'Location': booking.get_url()}


@api.route('/bookings/<int:id>', methods=['PUT'])
@json
def edit_booking(id):
    booking = Booking.query.get_or_404(id)
    booking.import_data(request.json)
    db.session.add(booking)
    db.session.commit()
    return {}



@api.route("/bookings/<int:booking_id>/send_notification/", methods=["POST"])
def send_notification(booking_id):
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Message is missing in the request data'}), 400
    message = data['message']
    booking = Booking.query.get_or_404(booking_id)
    booking_manager = BookingManager()
    booking_manager.send_notification(booking_id, message)
    return jsonify({'message': f'Notification sent for booking {booking_id}'}), 200


@api.route("/booking_reports/", methods=["GET"])
def generate_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if not start_date or not end_date:
        return jsonify({'error': 'Both start_date and end_date are required as query parameters'}), 400
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD format'}), 400
    booking_manager = BookingManager()
    report_data = booking_manager.generate_report(start_date, end_date)
    return jsonify(report_data), 200



@api.route("/bookings/<int:booking_id>/assign_caregiver/<int:caregiver_id>", methods=["POST"])
def assign_booking_to_caregiver(booking_id, caregiver_id):
    booking = BookingManager.query.get_or_404(booking_id)
    caregiver = Caregiver.query.get_or_404(caregiver_id)
    booking.assign_to_caregiver(caregiver)
    db.session.commit()
    return jsonify({"message": "Booking assigned to caregiver successfully"}), 200



@api.route("/bookings/<int:booking_id>/caregiver", methods=["GET"])
def get_caregiver_for_booking(booking_id):
    booking = BookingManager.query.get_or_404(booking_id)
    caregiver = booking.get_caregiver()
    if caregiver:
        return jsonify({"caregiver_id": caregiver.id}), 200
    else:
        return jsonify({"message": "No caregiver assigned to this booking"}), 404