import json
from fastapi import APIRouter, Request


router = APIRouter()


@router.get("/meli/notification")
async def read_root(request: Request):
    body = await request.body()

    if not body:
        return {"error": "El cuerpo de la solicitud está vacío"}
    
    json_body = json.loads(body.decode())
    parametros = request.query_params

    with open("meli.json", "w") as f:
        json.dump(json_body, f)

    return {"body": json_body, "params": dict(parametros)}

@router.get("/meli/credentials")
async def read_root(request: Request):
    body = await request.body()
    if not body:
        return {"error": "El cuerpo de la solicitud está vacío"}
    
    json_body = json.loads(body.decode())
    parametros = request.query_params

    with open("credential.json", "w") as f:
        json.dump(json_body, f)

    return {"body": json_body, "params": dict(parametros)}


__all__ = ["router"]