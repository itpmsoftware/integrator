import json
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os

load_dotenv()

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
async def read_root():

    url_redirect = "{}api/v1/meli/notification".format(os.getenv("APP_URL"))

    link_access = """https://auth.mercadolibre.com.co/authorization?response_type=code&client_id={}&redirect_uri={}""".format(os.getenv("APP_MELI_ID"), url_redirect)

    return RedirectResponse(url=link_access)


__all__ = ["router"]