from flask import Blueprint, render_template, request, jsonify, g
from sqlalchemy.orm import joinedload
from .models import City, Timestamp
from .services.weather_service import fetch_and_store_data
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home_view():
    if request.method == "POST":
        search = request.form.get("search-query")
        search_results = db.session.query(City).filter(City.name.ilike(f"%{search}%")).all()
        return render_template("search.html", search_city=search, search_result=search_results)

    return render_template("home.html")

@views.route('/main/<value>', methods=['POST', 'GET'])
def main_view(value):
    if request.method == "POST":
        search = request.form.get("search-query")
        search_results = db.session.query(City).filter(City.name.ilike(f"%{search}%")).all()
        return render_template("search.html", search_city=search, search_result=search_results)

    timestamps = Timestamp.query.options(joinedload(Timestamp.city)).filter(Timestamp.city.has(name=value)).all()
    return render_template("main.html", city=value, timestamp=timestamps) 

@views.route('/about', methods=['POST', 'GET'])
def about_view():
    if request.method == "POST":
        search = request.form.get("search-query")
        search_results = db.session.query(City).filter(City.name.ilike(f"%{search}%")).all()
        return render_template("search.html", search_city=search, search_result=search_results)

    return render_template("about.html")

@views.route('/contact', methods=['POST', 'GET'])
def contact_view():
    if request.method == "POST":
        search = request.form.get("search-query")
        search_results = db.session.query(City).filter(City.name.ilike(f"%{search}%")).all()
        return render_template("search.html", search_city=search, search_result=search_results)

    return render_template("contact.html")
