from nturl2path import url2pathname
import requests

# city_name = "Seattle,US"

def get_weather(api_key,lat,lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url,params={'units':'metric'}).json()

    weather = []
    temp = response['main']['temp']
    humidity = response['main']['humidity']
    desc = response['weather'][0]['description']
    icon = response['weather'][0]['icon']
    weather.append(temp)
    weather.append(humidity)
    weather.append(desc)
    weather.append(icon)
    return weather

def get_forecast(api_key,lat,lon):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url,params={'units':'metric'}).json()
    temps = []
    desc = []
    for i in response['daily']:
        temps.append(i['temp']['day'])
        desc.append(i['weather'][0]['description'])
    print(temps)
    print(desc)

# get_weather(api_key,lat,lon)