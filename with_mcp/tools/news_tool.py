import requests
import os


NEWS_API_KEY = os.getenv("NEWS_API_KEY")


tool = {
    "name": "news",
    "description": "Get latest news on any topic"
}


def execute(topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    data = response.json()

    articles = data["articles"][:5]

    result = ""

    for article in articles:
        result += f"- {article['title']}\n"

    return result