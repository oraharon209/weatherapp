import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_data(city_name):
    url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
           f'{city_name}?unitGroup=metric&include=days%2Chours&key={API_KEY}&contentType=json')
    try:
        result = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise StatusCodeException(f"status code error 500, API response failed")

    if result.status_code != 200:
        raise StatusCodeException(f"status code error {result.status_code}")
    data = result.json()
    parsed_data = parse_data(data)
    return {
        "country": parsed_data.get("country"),
        "forecast": parsed_data.get("forecast")
    }


def parse_data(data):
    country = data["resolvedAddress"]
    forecast = []
    for day in data["days"][:7]:
        day_name = datetime.strptime(day['datetime'], '%Y-%m-%d').strftime('%A')
        day_dict = {"date": day["datetime"],
                    "day_name": day_name,
                    "morning_temp": day["hours"][8]["temp"],
                    "evening_temp": day["hours"][20]["temp"],
                    "humidity": day["humidity"]}
        forecast.append(day_dict)

    return {
        "country": country,
        "forecast": forecast
    }


class StatusCodeException(Exception):
    pass
