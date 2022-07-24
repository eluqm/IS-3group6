#from crypt import methods
from ast import Pass
from operator import and_, or_
from queue import Empty
from sys import flags
from unittest.mock import patch
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)
#from flask_security import Security, roles_required, roles_accepted
#from flask_user import roles_required, UserManager

import os
import urllib.request

from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from huellaCarbono.models.interaccion import Interaccion
from huellaCarbono.models.post import Post
from huellaCarbono.models.role import Role
from huellaCarbono.models.user import User
from huellaCarbono.models.clasePublicacion import ClasePublicacion


from huellaCarbono.views.auth import login_required
from huellaCarbono.views.auth import admin_required
from huellaCarbono import db
from huellaCarbono import app

blog = Blueprint('blog', __name__, url_prefix='/blog')


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

# OBTENER UN USUARIO


def get_user(id):
    user = User.query.get_or_404(id)
    return user


def getPublicacion_by_id(id):
    return ClasePublicacion.query.get(id)


def getRole_by_id(id):
    return Role.query.get(id)


# LISTAR TODAS LAS PUBLICACIONES
@blog.route("/")
def index():
    updatePostLikes()
    posts = Post.query.all()
    posts = list(reversed(posts))
    interacciones = Interaccion.query.all()
    roles = Role.query.all()
    db.session.commit()
    db.session.commit()
    return render_template('blog/index.html', roles=roles, interacciones=interacciones,
                           posts=posts, get_user=get_user, functionInter=InteraccionUserInPosts,
                           getTipoPublicacion=getPublicacion_by_id,
                           getRole_by_id=getRole_by_id)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# REGISTRAR UN POST


@blog.route('/blog/create', methods=('GET', 'POST'))
@login_required
# @roles_required('admin')
# @roles_accepted('admin')
# @admin_required
def createPost():
    clasesPub = ClasePublicacion.query.all()
    db.session.commit()
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        tipoP = request.form.get('tipo')
        # to SAVE IMAGES
        filename = ""
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No se ha seleccionado una imagen")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #print("filename: ", filename)
            #print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(os.path.abspath(UPLOAD_FOLDER))
            #print(os.path.join('/home/russell', filename))
            #file.save(os.path.join(os.path.abspath(UPLOAD_FOLDER), filename))
            #file.save(os.path.join('/home/russell', filename))
            #file.save(os.path.join(os.path.abspath(UPLOAD_FOLDER), filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagen Guardado exitosamente")
        else:
            flash("Extensione spermitidas son: png, jpg, jpeg, gif")
            return redirect(request.url)
        # print(tipoP)
        post = Post(g.user.id, title, body, tipoP, filename)

        error = None
        if not title:
            flash('Se requiere un título')
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html', clasesPub=clasesPub)


@blog.route('/blog/createClasePublicación', methods=('GET', 'POST'))
@login_required
@admin_required
def createClasePublicacion():
    clasesPub = ClasePublicacion.query.all()
    db.session.commit()
    if request.method == 'POST':
        name = request.form.get('name')
        clasePublicacion = ClasePublicacion(name)
        if not name:
            flash('Se requiere un nombre para continuar')
        else:
            db.session.add(clasePublicacion)
            db.session.commit()
            return redirect(url_for('blog.createClasePublicacion'))

    return render_template('blog/createClasePublicacion.html', clasesPub=clasesPub)


# OBTENER POST
def get_post(id, check_author=True):
    post = Post.query.get(id)
    if post is None:
        abort(404, f'Id{id} de la publicaion no existe')
    if check_author and post.author != g.user.id:
        abort(404)
    return post


# UPDATE POST
@blog.route('/blog/update/<int:id>', methods=('GET', 'POST'))
@login_required
def updatePost(id):
    post = get_post(id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.body = request.form.get('body')

        if not post.title:
            flash('Se requiere un título')
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)


def updatePostLikes():
    posts = Post.query.all()
    for post in posts:
        post.interaccion_number = Interaccion.query.filter_by(
            post=post.id).count()
        db.session.add(post)
        db.session.commit()


# ELIMINAR POST
@blog.route('/blog/delete/<int:id>', methods=('GET', 'POST'))
@login_required
def deletePost(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))


@blog.route('/blog/meencanta/<int:id>', methods=('GET', 'POST'))
@login_required
def reaccionarPost(id):
    post = Post.query.get(id)
    #findUser = User.query.filter_by(username=username).first()
    # findInteraccion = Interaccion.query.filter(
    #    and_(Interaccion.user == g.user.id, Interaccion.post == post.id))
    # Student.query.filter_by(firstname='Sammy').all()
    findInteraccion = Interaccion.query.filter(and_(Interaccion.user == g.user.id,
                                                    Interaccion.post == post.id)).all()

    # finduser = User.query.filter(or_(User.username == 'pedro',
    #                                 User.username == 'elias'))
    if len(list(findInteraccion)) == 0:
        print("No lo encontro")
        # for row in findInteraccion:
        #    print("ID: ", row.id)
        # print(findInteraccion)
        interaccion = Interaccion(g.user.id, post.id)
        db.session.add(interaccion)
        db.session.commit()
    else:
        # print(list(findInteraccion))
        print("Si lo encontro")
        interacc = Interaccion.query.get(findInteraccion[0].id)
        db.session.delete(interacc)
        db.session.commit()
        # for row in findInteraccion:
        #print("ID: ", row.id)
        # print(findInteraccion[0].id) #THIS IS CORRECT
    return redirect(url_for('blog.index'))
