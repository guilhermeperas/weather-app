from flask import Blueprint, render_template
from app.services.weather_service import get_weather

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/weather")
def weather():
    get_weather("London")
    return
