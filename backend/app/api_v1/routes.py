
from flask_login import login_user, logout_user, login_required

from app import login_manager
from app.api_v1 import api


@api.route("/")
def get_homepage():
    return "<h1>We are Home</h1>"
