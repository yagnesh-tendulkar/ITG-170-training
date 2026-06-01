from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# FastAPI app
app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_with_ai(data: ChatRequest):

    response = model.generate_content(data.message)

    return {
        "user_message": data.message,
        "ai_response": response.text
    }