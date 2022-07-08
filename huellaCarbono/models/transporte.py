from datetime import datetime
from huellaCarbono import db


class Transporte(db.Model):
    __tablename__ = "transportes"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeigKey('users.id'), nullable=False)
    close_people = db.Column(db.Integer)
    hours_bus_week = db.Column(db.Integer)
    hours_train_week = db.Column(db.Integer)
    hours_vehicle_Week = db.Column(db.Integer)
    hours_metropolitan_week = db.Column(db.Integer)
    taxi_spending_week = db.Column(db.Integer)
    fuel_type = db.Column(db.String(15))
    fuel_spending = db.Column(db.Integer)
    vehicle_years = db.Column(db.Integer)
    vehicle_type = db.Column(db.String(15))
    hours_out_city_plane_year = db.Column(db.Integer)
    hours_out_city_bus_year = db.Column(db.Integer)
    hours_out_city_vehicle_year = db.Column(db.Integer)
    created = db.Column(db.Datatime, nullable=False,
                        default=datetime.utcnow)

    def __init__(self, user, close_people, hours_bus_week, hours_train_week, hours_vehicle_Week,
                 hours_metropolitan_week, taxi_spending_week, fuel_type, fuel_spending,
                 vehicle_years, vehicle_type, hours_out_city_plane_year, hours_out_city_bus_year,
                 hours_out_city_vehicle_year) -> None:
        self.user = user
        self.close_people = close_people
        self.hours_bus_week = hours_bus_week
        self.hours_train_week = hours_train_week
        self.hours_vehicle_Week = hours_vehicle_Week
        self.hours_metropolitan_week = hours_metropolitan_week
        self.taxi_spending_week = taxi_spending_week
        self.fuel_type = fuel_type
        self.fuel_spending = fuel_spending
        self.vehicle_years = vehicle_years
        self.vehicle_type = vehicle_type
        self.hours_out_city_plane_year = hours_out_city_plane_year
        self.hours_out_city_bus_year = hours_out_city_bus_year
        self.hours_out_city_vehicle_year = hours_out_city_vehicle_year

    def __repr__(self) -> str:
        # ajustar aqui
        return f'Close People: {self.close_people}'
