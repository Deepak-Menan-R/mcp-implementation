import requests
import os
from dotenv import load_dotenv


load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

print(f"NEWS_API_KEY: {NEWS_API_KEY}")  # Debug print

tool = {
    "name": "news",
    "description": "Get latest news on any topic"
}


def execute(topic):

    if not NEWS_API_KEY:
        return "ERROR: NEWS_API_KEY is not set"

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": topic,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    # Debug print
    print(data)

    # Handle API errors
    if data.get("status") != "ok":
        return f"ERROR: {data.get('message', 'Unknown error')}"

    articles = data.get("articles", [])[:5]

    if not articles:
        return "No news articles found."

    result = ""

    for article in articles:
        title = article.get("title", "No title")
        result += f"- {title}\n"

    return result