from huellaCarbono import db


class ClasePublicacion(db.Model):
    __tablename__ = 'clase_publicacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    def __init__(self, name) -> None:
        self.nombre = name
