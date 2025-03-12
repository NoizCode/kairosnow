from . import db
from sqlalchemy.sql import func

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_time = db.Column(db.String(100))
    temp = db.Column(db.Float)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    weather = db.Column(db.String(100))
    description = db.Column(db.String(100))
    wind = db.Column(db.Float)