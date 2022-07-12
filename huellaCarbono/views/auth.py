from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

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
        print(not username)
        print(not password)

        # error = None
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
                flash('lo siento mucho', "error")

    return render_template('auth/register.html')
