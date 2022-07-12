from flask import(
    render_Template, Blueprint, flash, g, redirect, request, url_for
)
from werkzeug.exceptions import abort
from huellaCarbono.models.post import Post
from huellaCarbono.models.user import User

from huellaCarbono.views.auth import login_required
from huellaCarbono import db

blog = Blueprint('blog', __name__)


# OBTENER UN USUARIO
def get_user(id):
    user = User.query.get_or_404(id)
    return user
