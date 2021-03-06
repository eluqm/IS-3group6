from datetime import datetime
from huellaCarbono import db
from huellaCarbono.models.clasePublicacion import ClasePublicacion
#from huellaCarbono.models.interaccion import Interaccion
from huellaCarbono.models.user import User
from sqlalchemy.orm import relationship


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    clase_post = db.Column(db.Integer, db.ForeignKey(
        'clase_publicacion.id'), nullable=False)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    interaccion_number = db.Column(db.Integer)
    pathImage = db.Column(db.String(100))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #users = relationship(User, cascade="all,delete", backref="children")
    users = relationship(User, backref=db.backref(
        "children01", cascade="all,delete"))

    clasePostPub = relationship(ClasePublicacion, backref=db.backref(
        "clasePulicacion", cascade="all,delete"))

    def __init__(self, author, title, body, tipoPublicacion, pathImage) -> None:
        self.author = author
        self.title = title
        self.interaccion_number = Post.query.filter_by(author=1).count()
  # Interaccion.query.count()
        self.body = body
        self.clase_post = tipoPublicacion
        self.pathImage = pathImage

    def __repr__(self) -> str:
        return f'Post: {self.title}'
