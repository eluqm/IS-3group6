from datetime import datetime
from huellaCarbono import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.foreigKey('users.id'), nullable=False)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    created = db.Column(db.DataTime, nuallable=False, default=datetime.utcnow)

    def __init(self, author, title, body) -> None:
        self.author = author
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'Post: {self.title}'
