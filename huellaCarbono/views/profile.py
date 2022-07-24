from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from huellaCarbono.views.auth import login_required
from huellaCarbono.views.auth import admin_required

profile = Blueprint('profile', __name__, url_prefix='/profile')


@profile.route("/profilee/<int:id>", methods=('GET', 'POST'))
@login_required
def perfil(id):
    return render_template('profile/profile.html')
