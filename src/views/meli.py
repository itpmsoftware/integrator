from typing import Optional
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os
import json


from src.controllers.meli import get_token_meli

load_dotenv()

router = APIRouter()


@router.get("/meli/notification")
async def read_root(code: Optional[str] = None):
    if(code):
        return await get_token_meli(code)
    else:
        return None

@router.post("/meli/notification")
async def read_root(request: Request):
    # Obtener el cuerpo de la solicitud
    body = await request.body()
    
    # Verificar si el cuerpo de la solicitud está vacío
    if not body:
        return {"error": "El cuerpo de la solicitud está vacío"}
    
    # Decodificar el cuerpo de la solicitud
    decoded_body = body.decode()
    
    # Cargar el cuerpo decodificado como JSON
    json_body = json.loads(decoded_body)
    
    # Obtener todos los parámetros de la solicitud
    parametros = request.query_params
    
    # Guardar json_body en un archivo .json
    with open("datos.json", "a") as f:
        json.dump(json_body, f)
    
    return {"body": json_body, "params": dict(parametros)}

@router.get("/meli/credentials")
async def read_root():

    url_redirect = "{}api/v1/meli/notification".format(os.getenv("APP_URL"))

    link_access = """https://auth.mercadolibre.com.co/authorization?response_type=code&client_id={}&redirect_uri={}""".format(os.getenv("APP_MELI_ID"), url_redirect)

    return RedirectResponse(url=link_access)


__all__ = ["router"]