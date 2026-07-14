from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import chat_with_ai

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI CRM Backend Running Successfully!"}

@app.post("/chat")
def chat(request: ChatRequest):
    reply = chat_with_ai(request.message)
    return {"reply": reply}