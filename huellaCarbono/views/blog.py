from crypt import methods
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
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


# LISTAR TODAS LAS PUBLICACIONES
@blog.route("/")
def index():
    posts = Post.query.all()
    db.session.commit()
    return render_template('blog/index.html', posts=posts, get_user=get_user)


# REGISTRAR UN POST
@blog.route('/blog/create', methods=('GET', 'POST'))
@login_required
def crearPost():
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
