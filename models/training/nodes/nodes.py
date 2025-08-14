from pydantic import BaseModel

class ChannelNode(BaseModel):
    """
    Represents a YouTube channel node.

    Fields:
    - title: The title of the YouTube channel.
    - channelId: Unique identifier of the channel.
    """
    title: str
    channelId : str


class VideoNode(BaseModel):
    """
    Represents a YouTube video node.

    Fields:
    - title: The title of the video.
    - videoId: Unique identifier of the video.
    - channel: An instance of ChannelOutput representing the channel that uploaded the video.
    """
    title : str
    videoId : str
    channel : ChannelNode


class CommentNode(BaseModel):
    """
    Represents a YouTube comment node.

    Fields:
    - id: Unique identifier of the comment.
    - textDisplay: Formatted text of the comment for display purposes.
    - textOriginal: Original text of the comment.
    - video: An instance of VideoOutput representing the video associated with the comment.
    """
    id : str
    textDisplay : str | None = None
    textOriginal : str | None = None
    category : str | None = None
    video : VideoNode


class TrainingComments(BaseModel):
    """
    Pydantic model representing a graph-like data structure for YouTube comments.

    Hierarchical structure:
    - `TrainingCommentOutput` contains a list of comments (`comments`).
    - Each `CommentOutput` represents a comment with its details and a reference to the associated video.
    - `VideoOutput` represents a video with its details and a reference to the YouTube channel that uploaded it.
    - `ChannelOutput` represents the YouTube channel with basic information.

    Main fields:
    - ChannelOutput:
        - `title`: the title of the YouTube channel.
        - `channelId`: unique identifier of the channel.
    - VideoOutput:
        - `title`: the title of the video.
        - `videoId`: unique identifier of the video.
        - `channel`: an instance of `ChannelOutput` representing the channel owning the video.
    - CommentOutput:
        - `id`: unique identifier of the comment.
        - `textDisplay`: formatted text of the comment for display.
        - `textOriginal`: original text of the comment.
        - `video`: an instance of `VideoOutput` representing the video related to the comment.
    - TrainingCommentOutput:
        - `comments`: a list of `CommentOutput` comments.

    This structure allows representing relationships between nodes (comments, videos, channels) in a nested manner,
    ideal for JSON serialization, data validation, and REST APIs returning hierarchical related data.
    """
    comments : list[CommentNode]

