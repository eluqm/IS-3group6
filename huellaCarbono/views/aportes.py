from huellaCarbono.utils.utils_profile import getUser
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)
from huellaCarbono import db
from huellaCarbono.views.auth import login_required
from huellaCarbono.views.auth import admin_required

aportes = Blueprint('aportes', __name__, url_prefix='/aportes')

# FROM UTILS


@aportes.route('/aportes/<int:id>', methods=('GET', 'POST'))
@login_required
def menu(id):
    user = getUser(id)
    return render_template('aportes/aportes.html', render="view/aportes")


@aportes.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errorPages/404.html'), 404


@aportes.errorhandler(401)
def unauthorized(e):
    # note that we set the 404 status explicitly
    return render_template('errorPages/401.html'), 401
