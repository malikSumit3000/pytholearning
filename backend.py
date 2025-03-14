import requests

API_key = '8c3303365d767a039c74bc0b4a9fa434'


def getdata(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)

    content = response.json()
    weather_data = content['list']
    required_data = weather_data[:forecast_days * 8]
    return required_data
    
