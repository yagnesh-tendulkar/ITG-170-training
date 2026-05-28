from fastapi import FastAPI
import google.generativeai as genai
app = FastAPI()
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
@app.get("/")
def home():
    return {"message": "Gemini API Running"}
@app.get("/ask")
def ask_gemini(question: str):
    response = model.generate_content(question)
    return {
        "question": question,
        "answer": response.text
    }