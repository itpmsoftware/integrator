from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/author")
def read_root():
    return {"author": "Sammy Guttman L."}


__all__ = ["router"]