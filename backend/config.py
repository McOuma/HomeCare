import os
from dotenv import load_dotenv
load_dotenv()

class Development:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
    SECRET_KEY = os.getenv("SECRET_KEY_DEV")
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class Testing:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_TEST')
    SECRET_KEY = os.getenv("SECRET_KEY_TEST")
