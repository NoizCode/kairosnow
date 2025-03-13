from . import db
from sqlalchemy.sql import func

class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    weather_timestamps = db.relationship('Timestamp', backref='city')

class Timestamp(db.Model):
    __tablename__ = "timestamps"

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    time = db.Column(db.String(100))
    temp = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    main_weath = db.Column(db.String(100))
    main_desc = db.Column(db.String(100))
    wind_speed = db.Column(db.Float)