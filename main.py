from fastapi import FastAPI
from pydantic import BaseModel
from routes.training.retrieve_entities import router as train_er_router
from routes.training.save_entities import router as save_entities_router

app = FastAPI()
app.include_router(train_er_router)
app.include_router(save_entities_router)