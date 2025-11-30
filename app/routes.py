from click import echo
from flask import Blueprint, render_template, request
from app.services.weather_service import get_weather

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/weather")
def weather():
    city = request.args.get("city")
    weather_data = get_weather(city)
    return render_template("index.html", weather=weather_data)
