from huellaCarbono import db
from huellaCarbono.models.role import Role
from huellaCarbono.models.user import User
from sqlalchemy.orm import relationship


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))

    users = relationship(User, backref=db.backref("children05", cascade="all,delete"))
    roles = relationship(Role, backref=db.backref("children06", cascade="all,delete"))


    def __init__(self) -> None:
        super().__init__()