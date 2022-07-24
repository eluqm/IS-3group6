from huellaCarbono.models.user import User
from huellaCarbono.models.post import Post
from huellaCarbono.models.interaccion import Interaccion
from huellaCarbono.models.clasePublicacion import ClasePublicacion
from huellaCarbono.models.role import Role

from flask import g, render_template
from werkzeug.exceptions import abort

from huellaCarbono import db

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


# OBTENER UN USUARIO
def get_user(id):
    user = User.query.get_or_404(id)
    return user


# obtener Una Clase de publicaion por id
def getPublicacion_by_id(id):
    return ClasePublicacion.query.get(id)


# OBTNER UNROL POR ID
def getRole_by_id(id):
    return Role.query.get(id)


# OBTENER UN POST POR SU ID
def get_post(id, check_author=True):
    post = Post.query.get(id)
    if post is None:
        #abort(404, f'Id{id} de la publicaion no existe')
        abort(404)
    if check_author and post.author != g.user.id:
        #abort(403, f'Id{id} forbidden')
        abort(401)
        # return render_template('errorPages/401.html'), 401
    return post

# ACTUALIZAR EL ATRBUTO interaccion_number CADA VEZ QUE ALGUIEN REACCIONA


def updatePostLikes():
    posts = Post.query.all()
    for post in posts:
        post.interaccion_number = Interaccion.query.filter_by(
            post=post.id).count()
        db.session.add(post)
        db.session.commit()


# DADO UN USUARIO , VER QUE POST LE GUSTO
def InteraccionUserInPosts(posts, interacciones, id):
    listReacciones = []
    for post in posts:
        flag = 0
        for inter in interacciones:
            if post.id == inter.post and inter.user == id:
                flag = 1
                listReacciones.append(True)
                break
        if not flag:
            listReacciones.append(False)
    return listReacciones


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
