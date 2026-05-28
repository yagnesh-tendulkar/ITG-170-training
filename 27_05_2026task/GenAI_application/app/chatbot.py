from groq import Groq
from dotenv import load_dotenv
import os
import asyncio
from typing import AsyncGenerator
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
async def chatbot_stream(
    message: str
) -> AsyncGenerator[str, None]:
    try:
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0.7,
            stream=True
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                await asyncio.sleep(0.01)
                yield content
    except Exception as e:
        yield f"ERROR: {str(e)}"
