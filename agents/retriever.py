from config import settings
import requests
from models.training.nodes.nodes import ChannelNode,VideoNode,CommentNode,TrainingComments
import json

class Retriever:
    def __init__(self,
                 url_retrieve_youtube_channel,
                 url_retrieve_video,
                 url_retrieve_comment):
        self.url_retrieve_youtube_channel=url_retrieve_youtube_channel
        self.url_retrieve_video=url_retrieve_video
        self.url_retrieve_comment=url_retrieve_comment

    def get_channel(self,name:str):
        try:
            channels=[]
            params_channels={"name": name}
            channels_res=requests.get(self.url_retrieve_youtube_channel,params_channels)
            json_channel=json.loads(channels_res.content)
            for channel in json_channel:
                channels.append(ChannelNode(title=channel['title'],channelId=channel['channelId']))
            return channels
        except Exception as e:
            raise e

    def get_videos(self,channel:ChannelNode,num_max_video:int) -> list[VideoNode]:
        videos=[]
        params_video={"channelId": channel.channelId,
                      "max_results": num_max_video}
        res=requests.get(self.url_retrieve_video,params_video)
        json_videos=json.loads(res.content)
        for item in json_videos:
            video=VideoNode(title=item['title'],videoId=item['videoId'],channel=channel)
            videos.append(video)
        return videos
    
    def get_comments(self,video:VideoNode,num_max_comments:int) -> TrainingComments:
        comments=[]
        try:
            params_comment={"videoId": video.videoId,
                            "max_results": num_max_comments}
            res=requests.get(self.url_retrieve_comment,params_comment)
            if res.status_code != 200:
                return TrainingComments(comments=[]) 
            json_comment=json.loads(res.content)
            for item in json_comment:
                comment=CommentNode(id=item['id'],
                                    textDisplay=item['textDisplay'],
                                    textOriginal=item['textOriginal'],
                                    video=video)
                comments.append(comment)
            return TrainingComments(comments=comments)
        except Exception as e:
            raise e
            
