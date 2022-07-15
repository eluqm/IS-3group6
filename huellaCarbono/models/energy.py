# THIS IS A ENERGY CATEGORY
from datetime import datetime
from huellaCarbono import db


class Energy(db.Model):
    __tablename__ = "energia"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    electricity_spending_month = db.Column(db.Float)
    created = db.Column(db.Datatime, nullable=False, default=datetime.utcnow)

    def __init__(self, user, electricity_spending):
        self.user = user
        self.electricity_spending_month = electricity_spending
