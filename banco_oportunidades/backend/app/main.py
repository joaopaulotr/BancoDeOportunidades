# main.py
# Ponto de entrada da API FastAPI

from fastapi import FastAPI
from . import routes

app = FastAPI()

app.include_router(routes.router)

