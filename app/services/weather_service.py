import requests
from dotenv import load_dotenv
import os

load_dotenv()
def get_weather(city):
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.json()
            return weather
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
