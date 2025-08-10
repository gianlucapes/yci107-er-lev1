from fastapi import FastAPI
from pydantic import BaseModel
from routes.training.retrieve_entities import router as train_er_router

app = FastAPI()
app.include_router(train_er_router)