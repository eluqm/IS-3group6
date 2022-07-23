from datetime import datetime
from huellaCarbono import db
from huellaCarbono.models.user import User
from huellaCarbono.models.post import Post

from sqlalchemy.orm import relationship


class Interaccion(db.Model):
    __tablename__ = "interacciones"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    users = relationship(User, backref=db.backref(
        "children02", cascade="all,delete"))
    posts = relationship(Post, backref=db.backref(
        "children03", cascade="all,delete"))

    def __init__(self, user, post) -> None:
        self.user = user
        self.post = post
