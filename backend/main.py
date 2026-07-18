from fastapi import FastAPI
from api.status import router as status_router

app = FastAPI()

app.include_router(status_router)