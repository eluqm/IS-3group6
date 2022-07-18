#from crypt import methods
from operator import and_, or_
from sys import flags
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)
from flask_security import Security, roles_required, roles_accepted
from pip import main
#from flask_user import roles_required, UserManager


from huellaCarbono.views.auth import login_required
from huellaCarbono.views.auth import admin_required
from huellaCarbono import db

main = Blueprint('index', __name__)


@main.route("/", methods=('GET', 'POST'))
def index():
    return render_template('index.html')
