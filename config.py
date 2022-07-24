# configuracion de produccion modo desarrollo
from flask_sqlalchemy import SQLAlchemy
UPLOAD_FOLDER = 'huellaCarbono/static/uploads/'


class Config:
    DEBUG = True
    TESTING = True

    # Configuracion de la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Angel1612@localhost:3306/huella_carbono"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/huella_carbono"

    # Flask-User settings
    # Shown in and email templates and page footers
    USER_APP_NAME = "Flask-User Basic App"
    USER_ENABLE_EMAIL = False        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
    USER_UNAUTHORIZED_ENDPOINT = "https://www.youtube.com/watch?v=FX0lMm_Qj10"

    UPLOAD_FOLDER = UPLOAD_FOLDER
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True
