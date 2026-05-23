import requests


tool = {
    "name": "weather",
    "description": "Get current weather for a city"
}


def execute(city):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    temp = current["temp_C"]

    humidity = current["humidity"]

    return f"""
Weather in {city}

Temperature: {temp}°C
Humidity: {humidity}%
"""