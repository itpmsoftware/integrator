from fastapi import HTTPException
from requests import post
from dotenv import load_dotenv
import os

load_dotenv()

async def get_token_meli(code: str):
    url = "https://api.mercadolibre.com/oauth/token"
    data = {
        "grant_type": 'authorization_code',
        "client_id": os.getenv("APP_MELI_ID"),
        "client_secret": os.getenv("APP_CLIENT_ID"),
        "code": code,
        "redirect_uri": "{}api/v1/meli/notification".format(os.getenv("APP_URL"))
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = await post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)