from crypt import methods
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


# LISTAR TODAS LAS PUBLICACIONES
@blog.route("/")
def index():
    posts = Post.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    return render_template('blog/index.html', posts=posts, get_user=get_user)


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
    interaccion = Interaccion(g.user.id, post.id)
    db.session.add(interaccion)
    db.session.commit()
    return redirect(url_for('blog.index'))
