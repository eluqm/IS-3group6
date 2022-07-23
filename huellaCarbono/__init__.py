from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_user import UserManager


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

from huellaCarbono.views.index import main
app.register_blueprint(main)

from huellaCarbono.views.blog import blog
app.register_blueprint(blog)



from huellaCarbono.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

admin = User('maria', generate_password_hash('maria'))
admin.setRole(1)
findUser = User.query.filter_by(username='maria').first()
if findUser == None:
    db.session.add(admin)
    db.session.commit()


#from huellaCarbono.models.user import User
#user_manager = UserManager(app, db, User)

db.create_all()

