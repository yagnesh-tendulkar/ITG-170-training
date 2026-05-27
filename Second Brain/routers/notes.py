from fastapi import APIRouter

from data.storage import notes

from schemas.note_schema import Note

router = APIRouter(
    prefix = "/notes",
    tags = ["notes"]
)

@router.get("/")
def get_notes():
    return notes

@router.post("/")
def create_notes(note : Note):
    notes.append(note)
    return{
        "message" : "Note Added Successfully",
        "note" : note
    }

@router.put("/{note_id}")
def update_notes(note_id : int,updated_note:Note):
    for i in range(len(notes)):
        if notes[i].id == note_id:
            notes[i] = updated_note

            return{
                "message" : "Note updated",
                "Notes" : notes
            }
    return {
        "message" : "not updated"
    }

@router.delete("/{note_id}")
def delete_notes(note_id: int):
    for i in range(len(notes)):
        if notes[i].id == note_id:
            notes.pop(i)

            return {
                "message" : "Note deleted"
            }
    return{
        "message" : "Note deletion unsuccessful"
    }




