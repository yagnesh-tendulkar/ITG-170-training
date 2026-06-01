import google.generativeai as genai

from core.config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


async def stream_gemini_response(prompt: str):

    try:

        response = model.generate_content(
            prompt,
            stream=True
        )

        for chunk in response:

            if chunk.text:
                yield chunk.text

    except Exception as e:

        yield f"Error: {str(e)}"