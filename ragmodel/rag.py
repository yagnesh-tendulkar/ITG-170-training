from pypdf import PdfReader
import numpy as np
import faiss
import json
import os

from sklearn.feature_extraction.text import TfidfVectorizer

# Global vectorizer
vectorizer = TfidfVectorizer()

# Store chunks in memory
stored_chunks = []


def read_pdf(path):
    """Extract text from PDF"""
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def chunk_text(text, size=500):
    """Split text into chunks"""

    chunks = []

    for i in range(0, len(text), size):
        chunks.append(text[i:i + size])

    return chunks


def create_embeddings(chunks):
    """Create TF-IDF vectors"""

    global vectorizer
    global stored_chunks

    stored_chunks = chunks

    embeddings = vectorizer.fit_transform(chunks)

    return embeddings.toarray()


def store_in_faiss(chunks, embeddings, db_path="vector_db"):
    """Store vectors in FAISS"""

    os.makedirs(db_path, exist_ok=True)

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(
        index,
        f"{db_path}/faiss_index.bin"
    )

    with open(
        f"{db_path}/chunks.json",
        "w"
    ) as f:

        json.dump(chunks, f)

    print(
        f"Stored {len(chunks)} chunks"
    )


def retrieve_similar_chunks(
    question,
    db_path="vector_db",
    top_k=3
):
    """Retrieve similar chunks"""

    if not os.path.exists(
        f"{db_path}/faiss_index.bin"
    ):
        return []

    index = faiss.read_index(
        f"{db_path}/faiss_index.bin"
    )

    with open(
        f"{db_path}/chunks.json",
        "r"
    ) as f:

        chunks = json.load(f)

    # Refit vectorizer on chunks
    vectorizer.fit(chunks)

    question_embedding = vectorizer.transform(
        [question]
    ).toarray()

    question_embedding = np.array(
        question_embedding,
        dtype=np.float32
    )

    distances, indices = index.search(
        question_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(chunks):
            results.append(
                chunks[idx]
            )

    return results