from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from website.services.weather_service import fetch_and_store_data
import os

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        from .models import City
        db.create_all()

    # Scheduler Setup
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_data, 'interval', minutes=60)
    scheduler.start()

    return app