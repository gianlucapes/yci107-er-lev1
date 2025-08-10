from pydantic import BaseModel

class TrainingCommentBody(BaseModel):
    channelNames: list[str]
    number_of_comments_per_video : int