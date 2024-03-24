from app.api_v1 import api


@api.route("/")
def get_homepage():
    return "<h1>We are Home</h1>"
