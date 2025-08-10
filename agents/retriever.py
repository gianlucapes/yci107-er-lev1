from config import settings
import requests
from models.training.output.comment import ChannelOutput
import json

class Retriever:
    def __init__(self,url_retrieve_youtube_channel,url_retrieve_video):
        self.url_retrieve_youtube_channel=url_retrieve_youtube_channel
        self.url_retrieve_video=url_retrieve_video

    def get_id_channel(self,name:str):
        try:
            channels=[]
            params_channels={"name": name}
            channels_res=requests.get(self.url_retrieve_youtube_channel,params_channels)
            json_channel_id=json.loads(channels_res.content)
            for channel_id in json_channel_id:
                channels.append(ChannelOutput(title=channel_id['title'],channelId=channel_id['channelId']))
            return channels
        except Exception as e:
            raise e

    def get_id_videos(self,channels:list[str]):
        videos=[]
        for channel in channels:
            params_videos={"channelId": channel}
            video_res=requests.get(self.url_retrieve_video,params_videos)
            json_video_id=json.loads(video_res.content)
            videos.append(json_video_id["videoId"])
        return videos