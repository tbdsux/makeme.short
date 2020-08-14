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
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/makemeshort"
    SECRET_KEY = "my-secret-key"


class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://nmdusrisgetesx:f1553d96c08224e8529608261ef42dbdc41447d1cd7416a9866b4f23db547876@ec2-34-197-188-147.compute-1.amazonaws.com:5432/d2rt3gp8n5ei5b"
    SECRET_KEY = os.getenv('SECRET_KEY')
