from huellaCarbono.models.user import User
from werkzeug.exceptions import abort
from flask import g


# obtner un Usuario pot su id
def getUser(id, check_author=True):
    user = User.query.get(id)
    if user is None:
        abort(404)
    if check_author and user.id != g.user.id:
        abort(401)
    return user
