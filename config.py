# configuracion de produccion modo desarrollo
from flask_sqlalchemy import SQLAlchemy


class Config:
    DEBUG = True
    TESTING = True

    # Configuracion de la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/huella_carbono"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True
