from fastapi import APIRouter,HTTPException
from config import settings
from urllib.parse import urljoin
from fastapi.responses import JSONResponse
from agents.retriever import Retriever
from models.training.request.comment import TrainingYCCommentRetrieveBody,TrainingVideoCommentRetrieveBody


router = APIRouter(prefix="/training_dataset/retrieve_entities")

base_url = settings.BASE_URL_LOCAL if settings.DEV else settings.BASE_URL
url_retrieve_youtube_channel=urljoin(base_url,settings.URL_RETRIEVE_YOUTUBE_CHANNEL)
url_retrieve_video=urljoin(base_url,settings.URL_RETRIEVE_VIDEO)
url_retrieve_comment=urljoin(base_url,settings.URL_RETRIEVE_COMMENT)
retriever=Retriever(url_retrieve_youtube_channel,
                            url_retrieve_video,
                            url_retrieve_comment)

@router.get("/youtube_channel/retrieve_comments",tags=["retrieve comments from youtube channel"])
def retrieve_comments_from_youtube_channels(channelNames: list[str],number_of_videos_per_channel : int,number_of_comments_per_video : int):
    try:
        res=[]
        trainingCommentRetrieveBody = TrainingYCCommentRetrieveBody(channelNames=channelNames,
                                                                    number_of_videos_per_channel=number_of_videos_per_channel,
                                                                    number_of_comments_per_video=number_of_comments_per_video)
        for item in trainingCommentRetrieveBody.channelNames:
            channels=retriever.get_channel(item)
            for channel in channels:
                videos=retriever.get_videos(channel=channel,num_max_video=trainingCommentRetrieveBody.number_of_videos_per_channel)
                comments=None
                for video in videos:
                    comments=retriever.get_comments(video=video,num_max_comments=trainingCommentRetrieveBody.number_of_comments_per_video)
                res.append(comments)
        return {"res": res}
    except Exception as e:
        return HTTPException(status_code=500, detail=e)

@router.post("/video/retrieve_comments")
def retrieve_comments_by_video(trainingCommentRetrieveBody : TrainingVideoCommentRetrieveBody):
    try:
        comments=retriever.get_comments(video=trainingCommentRetrieveBody.video,num_max_comments=trainingCommentRetrieveBody.number_of_comments)
        return {"res": comments}
    except Exception as e:
        return HTTPException(status_code=500, detail=e)



