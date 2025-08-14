from fastapi import APIRouter,HTTPException
from config import settings
from urllib.parse import urljoin
from models.training.nodes.nodes import TrainingComments
from db import neo4jService

router = APIRouter(prefix="/training_dataset/save_entities")

@router.post("/comments",tags=["save comments"])
def save_comments(trainingComments : TrainingComments):
    try:
        for item in trainingComments.comments:
            neo4jService.save_comments(item)
    except Exception as e:
        return HTTPException(status_code=500, detail=e)