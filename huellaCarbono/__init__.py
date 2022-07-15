from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# cargando las configuraciones
app.config.from_object('config.DevelopmentConfig')

app.jinja_env.filters['zip'] = zip



db = SQLAlchemy(app)

from huellaCarbono.views.blog import InteraccionUserInPosts
app.jinja_env.globals.update(InteraccionUserInPosts=InteraccionUserInPosts)


#IMPORTAR VISTAS
from huellaCarbono.views.auth import auth
app.register_blueprint(auth)

from huellaCarbono.views.blog import blog

app.register_blueprint(blog)

db.create_all()
