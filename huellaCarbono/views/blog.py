from operator import and_
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

import os
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from huellaCarbono.models.interaccion import Interaccion
from huellaCarbono.models.post import Post
from huellaCarbono.models.role import Role
from huellaCarbono.models.clasePublicacion import ClasePublicacion


from huellaCarbono.views.auth import login_required
from huellaCarbono.views.auth import admin_required
from huellaCarbono import db
from huellaCarbono import app

blog = Blueprint('blog', __name__, url_prefix='/blog')


# FROM UTILS
from huellaCarbono.utils.utils_blog import get_post
from huellaCarbono.utils.utils_blog import updatePostLikes
from huellaCarbono.utils.utils_blog import allowed_file
from huellaCarbono.utils.utils_blog import getRole_by_id
from huellaCarbono.utils.utils_blog import getPublicacion_by_id
from huellaCarbono.utils.utils_blog import get_user
from huellaCarbono.utils.utils_blog import InteraccionUserInPosts


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


@blog.route('/display/<filename>')
def displayImage(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


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


@blog.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errorPages/404.html'), 404


@blog.errorhandler(401)
def unauthorized(e):
    # note that we set the 404 status explicitly
    return render_template('errorPages/401.html'), 401
