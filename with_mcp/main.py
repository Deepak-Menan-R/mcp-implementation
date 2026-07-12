from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from pydantic import BaseModel

# -----------------------------------
# IMPORT TOOLS
# -----------------------------------

from with_mcp.tools.weather_tool import tool as weather_tool
from with_mcp.tools.exchange_tool import tool as exchange_tool
from with_mcp.tools.news_tool import tool as news_tool
from with_mcp.tools.email_tool import tool as email_tool

from with_mcp.tools.weather_tool import execute as weather_execute
from with_mcp.tools.exchange_tool import execute as exchange_execute
from with_mcp.tools.news_tool import execute as news_execute
from with_mcp.tools.email_tool import execute as email_execute


app = FastAPI()

templates = Jinja2Templates(directory="templates")


# -----------------------------------
# TOOL REGISTRY
# -----------------------------------

TOOLS = {
    "weather": {
        "metadata": weather_tool,
        "executor": weather_execute
    },

    "exchange_rate": {
        "metadata": exchange_tool,
        "executor": exchange_execute
    },

    "news": {
        "metadata": news_tool,
        "executor": news_execute
    },

    "email": {
        "metadata": email_tool,
        "executor": email_execute
    }
}


# -----------------------------------
# REQUEST MODEL
# -----------------------------------

class ChatRequest(BaseModel):
    message: str


# -----------------------------------
# SERVE FRONTEND
# -----------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# -----------------------------------
# SIMULATED LLM TOOL CHOOSING
# -----------------------------------

def llm_choose_tool(user_input):

    text = user_input.lower()

    # -----------------------------------
    # THIS SIMULATES MODEL REASONING
    # -----------------------------------

    if "weather" in text:

        return {
            "tool": "weather",
            "arguments": {
                "city": "Chennai"
            }
        }

    elif "exchange" in text or "rate" in text:

        return {
            "tool": "exchange_rate",
            "arguments": {
                "frm": "USD",
                "to": "INR"
            }
        }

    elif "news" in text:

        return {
            "tool": "news",
            "arguments": {
                "topic": "AI"
            }
        }

    return None


# -----------------------------------
# MAIN CHAT API
# -----------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    user_input = request.message

    # -----------------------------------
    # LLM CHOOSES TOOL DYNAMICALLY
    # -----------------------------------

    tool_call = llm_choose_tool(user_input)

    if not tool_call:

        return {
            "response": "No matching tool found"
        }

    tool_name = tool_call["tool"]

    arguments = tool_call["arguments"]

    # -----------------------------------
    # DYNAMIC TOOL EXECUTION
    # -----------------------------------

    executor = TOOLS[tool_name]["executor"]

    result = executor(**arguments)

    return {
        "response": result
    } 
