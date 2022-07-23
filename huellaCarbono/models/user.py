from huellaCarbono import db
from huellaCarbono.models.role import Role
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    rol = db.Column(db.Integer, db.ForeignKey(
        'roles.id'), nullable=False, default=2)
    #roles = db.relationship('Role', secondary='user_roles')
    roles = relationship(Role, backref=db.backref(
        "children04", cascade="all,delete"))

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'User: {self.username}'

    def setRole(self,role) -> None:
        self.rol = role