from datetime import datetime
from huellaCarbono import db


class Interaccion(db.Model):
    __tablename__ = "interacciones"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user, post) -> None:
        self.user = user
        self.post = post
