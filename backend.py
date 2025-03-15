import requests
import os

API_key = os.getenv("WEATHER_API_KEY")


def getdata(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    weather_data = content['list']
    required_data = weather_data[:forecast_days * 8]
    return required_data


if __name__ == "__main__":
    print(getdata(place="Newdelhi", forecast_days=3))
