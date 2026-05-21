from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from pydantic import BaseModel

from without_mcp.app.weather import get_weather
from without_mcp.app.exchange import get_exchange_rate
from without_mcp.app.news import get_news


app = FastAPI()

# -----------------------------------
# Templates
# -----------------------------------

templates = Jinja2Templates(directory="templates")


# -----------------------------------
# Request Schema
# -----------------------------------

class ChatRequest(BaseModel):
    message: str


# -----------------------------------
# Serve HTML Page
# -----------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# -----------------------------------
# ENTITY EXTRACTION
# -----------------------------------

def extract_city(text):

    cities = ["chennai", "bangalore", "delhi", "mumbai"]

    for city in cities:
        if city in text.lower():
            return city

    return "Chennai"


def extract_topic(text):

    topics = ["ai", "sports", "technology", "finance"]

    for topic in topics:
        if topic in text.lower():
            return topic

    return "technology"


# -----------------------------------
# CHAT ROUTER
# -----------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    user_input = request.message

    text = user_input.lower()

    # ----------------------------------
    # HARD CODED ROUTING 😬
    # ----------------------------------

    if "weather" in text:

        city = extract_city(text)

        result = get_weather(city)

        return {
            "response": result
        }

    # ----------------------------------

    elif "exchange" in text or "rate" in text:

        result = get_exchange_rate("USD", "INR")

        return {
            "response": result
        }

    # ----------------------------------

    elif "news" in text:

        topic = extract_topic(text)

        news_result = get_news(topic)

        return {
            "response": news_result
        }

    # ----------------------------------

    else:

        return {
            "response": "Sorry, I don't understand."
        }