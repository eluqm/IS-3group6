from functools import wraps
#from flask_login import current_user
from flask import abort
import functools
from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

#from flask_user import login_required, UserManager, UserMixin
#from flask_login import current_user

from huellaCarbono.models.user import User
from huellaCarbono import db
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__, url_prefix='/auth')


# registrar un usuario
@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username, generate_password_hash(password))

        if not username:
            flash('Se requiere nombre de usuario', "error")
        if not password:
            flash('Se requiere contraseña', "error")
        if username and password:
            findUser = User.query.filter_by(username=username).first()
            if findUser == None:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('auth.login'))
            else:
                flash(f'El usuario {username} ya esta registrado', "error")

    return render_template('auth/register.html')


# INICIAR SESION
@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = None
        findUser = User.query.filter_by(username=username).first()

        if not findUser:
            error = 'Usuario no registrado'
            flash('Usuario no Regisrado')
        else:
            if not check_password_hash(findUser.password, password):
                error = 'contraseña incorrecta'
                flash('contraseña incorrecta')

            if error == None:
                session.clear()
                session['user_id'] = findUser.id
                return redirect(url_for('index.index'))  # update line
            # flash(error)

    return render_template('auth/login.html')


# VERIFICAR QUE EL USUARIO ESTE LOGEADO
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        #g.user = User.query.get_or_404(user_id)
        g.user = User.query.get(user_id)


# LOGOUT
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.index'))


# INICIAR SESION  REQUERIDO PARA ACTIVIDADES(crear,editar,etc)
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(g.user, 'username', False)
        if is_admin != 'admin':
            # if not is_admin:
            # abort(401)
            # return render_template('404.html'), 404
            return render_template('errorPages/401.html'), 401
        return f(*args, **kws)
    return decorated_function
