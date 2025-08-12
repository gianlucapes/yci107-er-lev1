from fastapi import APIRouter,HTTPException
from config import settings
from urllib.parse import urljoin
from models.training.nodes.comment import TrainingComments

router = APIRouter(prefix="/training_dataset/save_entities")

@router.post("/comments",tags=["save comments"])
def save_comments(trainingComments : TrainingComments):
    try:
        pass
    except Exception as e:
        return HTTPException(status_code=500, detail=e)