from fastapi import APIRouter
from config import settings
from urllib.parse import urljoin
from fastapi.responses import JSONResponse
from utils.retriever import Retriever


router = APIRouter()

@router.post("/retrieve")
def retrieve_dataset_from_youtube(channelName : list[str]):
    try:
        res=[]
        base_url = settings.BASE_URL_LOCAL if settings.LOCAL else settings.BASE_URL
        url_retrieve_youtube_channel=urljoin(base_url,settings.URL_RETRIEVE_YOUTUBE_CHANNEL)
        url_retrieve_video=urljoin(base_url,settings.URL_RETRIEVE_VIDEO)
        retriever=Retriever(url_retrieve_youtube_channel,url_retrieve_video)
        for item in channelName:
            channelId=retriever.get_id_channel(item)
            videoId=retriever.get_id_videos(channelId)
            res.append({"channelId":channelId,"videoId":videoId})
        return {"message": res}
    except Exception as e:
        return JSONResponse(e)
    
