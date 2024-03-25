from datetime import datetime, timedelta

from flask import jsonify, request, url_for

from .. import db
from ..models import Service
from . import api
from .decorators import json, paginate


@api.route("/services/<int:id>/", methods=["GET"])
@json
def get_service(id):
    service = Service.query.get_or_404(id)
    return jsonify(service.export_data())


@api.route("/services/", methods=["POST"])
@json
def create_service():
    data = request.get_json()
    service = Service()
    service.import_data(data)
    db.session.add(service)
    db.session.commit()
    response = jsonify(service.export_data())
    response.status_code = 201
    response.headers["Location"] = service.get_url()
    return response


@api.route("/services/<int:id>/", methods=["PUT"])
@json
def update_service(id):
    service = Service.query.get_or_404(id)
    data = request.get_json()
    service.import_data(data)
    db.session.commit()
    return jsonify(message="Service information updated successfully")


@api.route("/services/<int:id>/", methods=["DELETE"])
@json
def delete_service(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify(message="Service deleted successfully")


@api.route("/services/<int:service_id>/bookings/", methods=["GET"])
def list_bookings(service_id):
    service = Service.query.get_or_404(service_id)
    bookings = service.bookings.all()
    booking_data = [booking.export_data() for booking in bookings]
    return jsonify({"bookings": booking_data}), 200


@api.route("/services/<int:service_id>/revenue/", methods=["GET"])
def calculate_revenue(service_id):
    service = Service.query.get_or_404(service_id)
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    if not (start_date and end_date):
        return (
            jsonify({"message": "Start date and end date are required parameters."}),
            400,
        )
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    total_revenue = service.calculate_revenue(start_date, end_date)
    return jsonify({"total_revenue": total_revenue}), 200
