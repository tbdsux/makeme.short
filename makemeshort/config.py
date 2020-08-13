# from dotenv import load_dotenv
import os

# load_dotenv()  # > enable when running in venv


class Config:
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_DEFAULT_SENDER = "no-reply@makeme.short"
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/makemeshort"
    SECRET_KEY = "my-secret-key"


class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
