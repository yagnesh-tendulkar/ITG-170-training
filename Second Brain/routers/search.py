from fastapi import APIRouter

from data.storage import notes, snippets


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search_data(q: str):

    matched_notes = []
    matched_snippets = []

    for note in notes:

        if q.lower() in note.title.lower():

            matched_notes.append(note)

    for snippet in snippets:

        if q.lower() in snippet.title.lower():

            matched_snippets.append(snippet)

    return {
        "notes": matched_notes,
        "snippets": matched_snippets
    }