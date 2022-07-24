from huellaCarbono.utils.utils_profile import getUser
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)
from huellaCarbono import db
from huellaCarbono.views.auth import login_required
from huellaCarbono.views.auth import admin_required

profile = Blueprint('profile', __name__, url_prefix='/profile')

# FROM UTILS


@profile.route("/information/<int:id>", methods=('GET', 'POST'))
@login_required
def perfil(id):
    user = getUser(id)
    if request.method == 'POST':
        user.username = request.form.get('username')
        if not user.username:
            flash('Se requiere Username')
        else:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('profile.perfil'))
    return render_template('profile/profile.html')


@profile.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errorPages/404.html'), 404


@profile.errorhandler(401)
def unauthorized(e):
    # note that we set the 404 status explicitly
    return render_template('errorPages/401.html'), 401
