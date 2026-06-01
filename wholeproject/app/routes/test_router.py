from fastapi import APIRouter, HTTPException, status
from app.database.database import dbTest
from app.schemas.schemes import Test

router = APIRouter(
    prefix="/test",
    tags=["task"]
)

@router.post("/test", status_code=status.HTTP_201_CREATED)
async def create_test(test: Test):

    if test.id in dbTest:
        raise ValueError(
            status_code=status.HTTP_ALREADY_EXISTS,
            detail="The record already exists!"
        )

    dbTest[test.id] = test
    return test


@router.get("/test")
async def get_test():
    return list(dbTest.values())


@router.get("/test/{test_id}")
async def get_test_id(test_id: int):

    result = dbTest.get(test_id)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found "
        )

    return result


@router.put("/test/{test_id}")
async def update_test(test_id: int, updated_test: Test):

    if test_id not in dbTest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user not found"
        )

    updated_test.id = test_id
    dbTest[test_id] = updated_test

    return updated_test


@router.delete("/test/{test_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(test_id: int):

    if test_id not in dbTest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user not found"
        )

    del dbTest[test_id]
    return None