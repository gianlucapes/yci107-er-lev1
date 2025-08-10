from fastapi import APIRouter,HTTPException
from config import settings
from urllib.parse import urljoin
from fastapi.responses import JSONResponse
from agents.retriever import Retriever
from models.training.request.comment import TrainingCommentBody


router = APIRouter(prefix="/training_dataset")

@router.post("/retrieve_comments")
def retrieve_comments_from_youtube_channels(channelName : TrainingCommentBody):
    try:
        res=[]
        base_url = settings.BASE_URL_LOCAL if settings.DEV else settings.BASE_URL
        url_retrieve_youtube_channel=urljoin(base_url,settings.URL_RETRIEVE_YOUTUBE_CHANNEL)
        url_retrieve_video=urljoin(base_url,settings.URL_RETRIEVE_VIDEO)
        retriever=Retriever(url_retrieve_youtube_channel,url_retrieve_video)
        for item in channelName:
            channel=retriever.get_id_channel(item)
            res.append(channel)
        return {"message": res}
    except Exception as e:
        return HTTPException(status_code=500, detail=e)
    
