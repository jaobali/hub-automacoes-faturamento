from fastapi import FastAPI
from models.calculadora import somar

app = FastAPI()

@app.get("/somar")
def rota_somar(a: int, b: int):
    return {"resultado": somar(a, b)}