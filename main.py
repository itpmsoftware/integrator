from fastapi import FastAPI

from src.controllers import router_test, router_meli

app = FastAPI()


app.include_router(router_test, prefix="/api/v1")
app.include_router(router_meli, prefix="/api/v1")