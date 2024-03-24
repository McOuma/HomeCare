from flask import Blueprint
from app.auth import login_required, token_required

api = Blueprint("api", __name__)


@api.before_request
@login_required
def before_request():
    """All routes in this blueprint require authentication."""
    pass


@api.after_request
def after_request(response):
    pass





from . import booking, booking_manager,caregiver,client,errors,review,service,user