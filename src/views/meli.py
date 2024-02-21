import json
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os


from src.controllers.meli import get_token_meli

load_dotenv()

router = APIRouter()


@router.get("/meli/notification")
async def read_root(code: str):
    return await get_token_meli(code)

@router.get("/meli/credentials")
async def read_root():

    url_redirect = "{}api/v1/meli/notification".format(os.getenv("APP_URL"))

    link_access = """https://auth.mercadolibre.com.co/authorization?response_type=code&client_id={}&redirect_uri={}""".format(os.getenv("APP_MELI_ID"), url_redirect)

    return RedirectResponse(url=link_access)


__all__ = ["router"]