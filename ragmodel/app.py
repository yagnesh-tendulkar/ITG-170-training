from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import read_pdf, chunk_text, create_embeddings, store_in_faiss, retrieve_similar_chunks
import os

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(
    directory="templates"
)

# Create uploads folder if it doesn't exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("vector_db", exist_ok=True)

class QuestionRequest(BaseModel):
    """Format for questions from the frontend"""
    question: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/upload")
async def upload_pdf(pdf: UploadFile = File(...)):
    """
    RAG Pipeline Step 1: Upload and Process PDF
    
    Steps:
    1. Save PDF file
    2. Extract text from PDF
    3. Split text into chunks
    4. Create embeddings for each chunk
    5. Store in FAISS database
    """
    
    # Step 1: Save the PDF
    pdf_path = f"uploads/{pdf.filename}"
    with open(pdf_path, "wb") as file:
        file.write(await pdf.read())
    
    # Step 2: Extract text from PDF
    text = read_pdf(pdf_path)
    
    # Step 3: Split into chunks
    chunks = chunk_text(text, size=500)
    
    # Step 4: Create embeddings (convert text to vectors)
    embeddings = create_embeddings(chunks)
    
    # Step 5: Store in FAISS database
    store_in_faiss(chunks, embeddings)
    
    return {
        "message": "PDF uploaded and processed!",
        "chunks_created": len(chunks)
    }

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    RAG Pipeline Step 2: Answer Questions
    
    Steps:
    1. Get the user's question
    2. Find similar chunks from the PDF
    3. Use those chunks as context
    4. Generate an answer
    """
    
    question = request.question
    
    # Step 1: Retrieve relevant chunks from FAISS
    relevant_chunks = retrieve_similar_chunks(question, top_k=3)
    
    if not relevant_chunks:
        return {
            "answer": "No PDF uploaded yet. Please upload a PDF first.",
            "sources": []
        }
    
    # Step 2: Create context from relevant chunks
    context = "\n".join(relevant_chunks)
    
    # Step 3: Create a simple answer by combining context
    # (In production, you'd use an LLM like GPT, Ollama, etc.)
    answer = f"Based on the document:\n\n{context}"
    
    return {
        "answer": answer,
        "sources": relevant_chunks
    }