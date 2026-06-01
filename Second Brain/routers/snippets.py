from fastapi import APIRouter

from schemas.snippet_schema import Snippet
from data.storage import snippets


router = APIRouter(
    prefix="/snippets",
    tags=["Snippets"]
)


@router.get("/")
def get_snippets():
    return snippets


@router.post("/")
def create_snippet(snippet: Snippet):

    snippets.append(snippet)

    return {
        "message": "Snippet added successfully",
        "snippet": snippet
    }


@router.get("/{snippet_id}")
def get_single_snippet(snippet_id: int):

    for snippet in snippets:

        if snippet.id == snippet_id:
            return snippet

    return {
        "message": "Snippet not found"
    }


@router.delete("/{snippet_id}")
def delete_snippet(snippet_id: int):

    for i in range(len(snippets)):

        if snippets[i].id == snippet_id:

            snippets.pop(i)

            return {
                "message": "Snippet deleted successfully"
            }

    return {
        "message": "Snippet not found"
    }