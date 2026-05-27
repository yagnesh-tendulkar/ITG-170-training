from fastapi import APIRouter, HTTPException
from forth_question.app_status import AppStatus

router = APIRouter()

icecreams = []


# CREATE
@router.post("/icecreams")
async def add_icecream():

    data = {
        "id": 1,
        "flavor": "Chocolate"
    }

    icecreams.append(data)

    return {
        "status": AppStatus.HTTP_201_CREATED,
        "message": AppStatus.ICECREAM_CREATED,
        "data": data
    }


# GET
@router.get("/icecreams")
async def get_icecreams():

    return {
        "status": AppStatus.HTTP_200_OK,
        "data": icecreams
    }


# UPDATE
@router.put("/icecreams/{icecream_id}")
async def update_icecream(icecream_id: int):

    if not icecreams:

        raise HTTPException(
            status_code=AppStatus.HTTP_404_NOT_FOUND,
            detail=AppStatus.ICECREAM_NOT_FOUND
        )

    icecreams[0]["flavor"] = "Vanilla"

    return {
        "status": AppStatus.HTTP_200_OK,
        "message": AppStatus.ICECREAM_UPDATED,
        "data": icecreams[0]
    }


# DELETE
@router.delete("/icecreams/{icecream_id}")
async def delete_icecream(icecream_id: int):

    if not icecreams:

        raise HTTPException(
            status_code=AppStatus.HTTP_404_NOT_FOUND,
            detail=AppStatus.ICECREAM_NOT_FOUND
        )

    icecreams.clear()

    return {
        "status": AppStatus.HTTP_200_OK,
        "message": AppStatus.ICECREAM_DELETED
    }