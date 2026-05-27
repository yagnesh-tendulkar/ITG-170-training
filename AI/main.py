
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import google.generativeai as genai
import asyncio
import os

app = FastAPI(title="Gemini Streaming API")

# ---------------- GEMINI CONFIG ----------------
GOOGLE_API_KEY = "AIzaSyDDr3dUFHEQCIMBeunSdmmcl3Nn0tIQiLQ"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------- STREAM FUNCTION ----------------
async def stream_response(prompt: str):
    """
    Streams response like ChatGPT using yield
    """

    response = model.generate_content(prompt, stream=True)

    for chunk in response:
        if chunk.text:
            # simulate streaming delay (optional but makes it real-time feel)
            await asyncio.sleep(0.02)

            yield chunk.text


# ---------------- API ENDPOINT ----------------
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    if not prompt:
        return {"error": "Prompt is required"}

    return StreamingResponse(
        stream_response(prompt),
        media_type="text/plain"
    )


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )