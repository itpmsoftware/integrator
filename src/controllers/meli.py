from fastapi import APIRouter


router = APIRouter()


@router.get("/meli/notification")
def read_root(response):
    return response


__all__ = ["router"]