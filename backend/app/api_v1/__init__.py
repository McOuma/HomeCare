from flask import Blueprint

from ..auth import auth
from .decorators import etag, rate_limit

api = Blueprint("api", __name__)

# @api.route('/')
# def home_page():
#     return "<h1>Welcome Home</h1>"


@api.before_request
@rate_limit(limit=5, period=15)
@auth.login_required
def before_request():
    """All routes in this blueprint require authentication."""
    pass


@api.after_request
@etag
def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv


from . import booking, booking_manager, caregiver, client, errors, review, service, user
