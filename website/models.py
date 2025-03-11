from . import db
from sqlalchemy.sql import func

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    temp = db.Column(db.Integer)
    rain = db.Column(db.Boolean)