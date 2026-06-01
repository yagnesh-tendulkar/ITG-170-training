import mimetypes
from pathlib import Path

import PyPDF2
import docx

from exceptions import FileException, NotFoundException

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

SUPPORTED_EXTENSIONS = {".pdf", ".docx"}


def _build_filename(task_id: int, user_id: int, suffix: str) -> str:
    return f"{user_id}_{task_id}{suffix}"


def _find_saved_file(task_id: int, user_id: int) -> Path:
    matches = list(UPLOAD_DIR.glob(f"{user_id}_{task_id}.*"))
    if not matches:
        raise NotFoundException("Uploaded file not found")
    return matches[0]


def _guess_extension(filename: str, content_type: str | None) -> str:
    suffix = Path(filename).suffix.lower() if filename else ""
    if suffix:
        return suffix
    guessed = mimetypes.guess_extension(content_type or "")
    return guessed or ".bin"


def _extract_text_from_docx(file_path: Path) -> str:
    try:
        document = docx.Document(file_path)
        return "\n".join(paragraph.text for paragraph in document.paragraphs if paragraph.text)
    except Exception as exc:
        raise FileException(f"Unable to extract text from DOCX: {exc}")


def _extract_text_from_pdf(file_path: Path) -> str:
    try:
        text_parts = []
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
        return "\n\n".join(text_parts).strip()
    except Exception as exc:
        raise FileException(f"Unable to extract text from PDF: {exc}")


def extract_text_from_file(task_id: int, user_id: int) -> dict[str, str]:
    file_path = _find_saved_file(task_id, user_id)
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        extracted = _extract_text_from_pdf(file_path)
    elif suffix == ".docx":
        extracted = _extract_text_from_docx(file_path)
    else:
        raise FileException("Unsupported file format for text extraction")

    return {
        "task_id": task_id,
        "filename": file_path.name,
        "content_type": mimetypes.guess_type(file_path.name)[0] or "application/octet-stream",
        "extracted_text": extracted,
    }


async def upload_file_service(task_id: int, user_id: int, file):
    try:
        suffix = _guess_extension(file.filename, getattr(file, "content_type", None))
        filename = _build_filename(task_id, user_id, suffix)
        file_path = UPLOAD_DIR / filename
        content = await file.read()

        with open(file_path, "wb") as f:
            f.write(content)

        extraction = None
        if suffix in SUPPORTED_EXTENSIONS:
            extraction = extract_text_from_file(task_id, user_id)
    except Exception as exc:
        raise FileException(f"Unable to upload file: {exc}")

    response = {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "stored_path": str(file_path),
    }
    if extraction:
        response["extracted_text"] = extraction["extracted_text"]
    return response


def stream_file_service(task_id: int, user_id: int):
    file_path = _find_saved_file(task_id, user_id)

    def file_iterator():
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                yield chunk

    return file_iterator()


def generate_chat_response(extracted_text: str, prompt: str, max_tokens: int = 200) -> str:
    if not extracted_text.strip():
        return "No text is available for this task. Upload a supported PDF or DOCX file first."

    search_target = prompt.strip()
    if not search_target:
        return extracted_text[:max_tokens].strip()

    lower_text = extracted_text.lower()
    lower_prompt = search_target.lower()
    idx = lower_text.find(lower_prompt)
    if idx < 0:
        snippet = extracted_text[:max_tokens]
        return snippet.strip() + ("..." if len(extracted_text) > max_tokens else "")

    start = idx + len(search_target)
    remaining = extracted_text[start:].strip()
    if not remaining:
        return "Prompt found at the end of the document; there is no following text."

    if len(remaining) <= max_tokens:
        return remaining

    snippet = remaining[:max_tokens]
    last_space = snippet.rfind(" ")
    if last_space > 0:
        snippet = snippet[:last_space]
    return snippet.strip() + "..."
