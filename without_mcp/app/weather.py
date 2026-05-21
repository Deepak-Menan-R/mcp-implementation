import requests


def get_weather(city):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    temp = current["temp_C"]

    humidity = current["humidity"]

    feels_like = current["FeelsLikeC"]

    return f"""
Weather Report for {city}

Temperature: {temp}°C
Feels Like: {feels_like}°C
Humidity: {humidity}%
"""