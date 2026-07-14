from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from graph import graph

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI CRM Backend Running Successfully"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=request.message)
            ]
        }
    )

    print(result)

    final_message = result["messages"][-1]

    return {
        "response": getattr(final_message, "content", str(final_message))
    }