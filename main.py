from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from contextlib import asynccontextmanager
from routes.massive_insert_channels import router as massive_insert_router

app = FastAPI()
app.include_router(massive_insert_router)