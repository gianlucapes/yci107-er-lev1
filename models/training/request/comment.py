from pydantic import BaseModel
from models.training.nodes.nodes import ChannelNode,VideoNode

class TrainingYCCommentRetrieveBody(BaseModel):
    channelNames: list[str]
    number_of_videos_per_channel : int
    number_of_comments_per_video : int

class TrainingVideoCommentRetrieveBody(BaseModel):
    video : VideoNode
    number_of_comments : int

