import requests
import os


NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news(topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])[:5]

    if not articles:
        return "No news found"

    result = ""

    for index, article in enumerate(articles):

        result += f"{index + 1}. {article['title']}\n\n"

    return result