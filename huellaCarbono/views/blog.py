from crypt import methods
from operator import and_, or_
from queue import Empty
from sys import flags
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)
from werkzeug.exceptions import abort
from huellaCarbono.models.interaccion import Interaccion
from huellaCarbono.models.post import Post
from huellaCarbono.models.user import User

from huellaCarbono.views.auth import login_required
from huellaCarbono import db

blog = Blueprint('blog', __name__)


# OBTENER UN USUARIO
def get_user(id):
    user = User.query.get_or_404(id)
    return user


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


# LISTAR TODAS LAS PUBLICACIONES
@blog.route("/")
def index():
    posts = Post.query.all()
    posts = list(reversed(posts))
    interacciones = Interaccion.query.all()
    db.session.commit()
    db.session.commit()
    return render_template('blog/index.html', interacciones=interacciones,
                           posts=posts, get_user=get_user, functionInter=InteraccionUserInPosts)


# REGISTRAR UN POST
@blog.route('/blog/create')
@login_required
def createPost():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        post = Post(g.user.id, title, body)

        error = None
        if not title:
            flash('Se requiere un título')
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


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
