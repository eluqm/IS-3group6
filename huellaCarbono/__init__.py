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

from huellaCarbono.views.blog import getRole_by_id
app.jinja_env.globals.update(getRole_by_id=getRole_by_id)

#IMPORTAR VISTAS
from huellaCarbono.views.auth import auth
app.register_blueprint(auth)

from huellaCarbono.views.index import main
app.register_blueprint(main)

from huellaCarbono.views.blog import blog
app.register_blueprint(blog)

from huellaCarbono.views.profile import profile
app.register_blueprint(profile)


from huellaCarbono.views.aportes import aportes
app.register_blueprint(aportes)



#from huellaCarbono.models.user import User
#user_manager = UserManager(app, db, User)

db.create_all()

from huellaCarbono.models.role import Role
roleadmin = Role('admin')
roleUser= Role('user')
findRoleAdmin = Role.query.filter_by(name='admin').first()
findRoleUser = Role.query.filter_by(name='user').first()
if findRoleAdmin == None:
    db.session.add(roleadmin)
    db.session.commit()
if findRoleUser == None:
    db.session.add(roleUser)
    db.session.commit()

from huellaCarbono.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

admin = User('admin', generate_password_hash('admin'))
admin.setRole(1)
findUser = User.query.filter_by(username='admin').first()
if findUser == None:
    db.session.add(admin)
    db.session.commit()
