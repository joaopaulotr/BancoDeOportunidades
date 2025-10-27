# main.py
# Ponto de entrada da API FastAPI

from fastapi import FastAPI

from .routes import router

app = FastAPI()

app.include_router(router)

