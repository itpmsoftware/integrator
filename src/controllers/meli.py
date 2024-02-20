import json
from fastapi import APIRouter, Request


router = APIRouter()


@router.get("/meli/notification")
async def read_root(request: Request):
    body = await request.body()
    json_body = json.loads(body.decode())

    with open("meli.json", "w") as f:
        json.dump(json_body, f)

    return json_body

@router.get("/meli/credentials")
async def read_root(request: Request):
    body = await request.body()
    json_body = json.loads(body.decode())

    with open("credential.json", "w") as f:
        json.dump(json_body, f)

    return json_body


__all__ = ["router"]