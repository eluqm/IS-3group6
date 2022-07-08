from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# cargando las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
db.create_all()
