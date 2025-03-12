from flask import Blueprint, render_template, request, jsonify, g
from sqlalchemy.orm import joinedload
from .models import City, Timestamp
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home_view():
    if request.method == "POST":
        city = request.form.get("search-query")

    return render_template("home.html")

@views.route('/main/<value>', methods=['POST', 'GET'])
def main_view(value):
    return render_template("main.html", city=value) 

@views.route('/about', methods=['GET'])
def about_view():
    return render_template("about.html")

@views.route('/contact', methods=['GET'])
def contact_view():
    return render_template("contact.html")