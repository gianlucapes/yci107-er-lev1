from models.training.nodes.nodes import CommentNode

class Neo4jService:
    def __init__(self,driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def save_comments(self,comment:CommentNode):
        try:
            with self.driver.session() as session:
                session.run("""
                    // Channel Node
                    MERGE (c:Channel {channelId: $channelId})
                    ON CREATE SET c.title = $channelTitle
                    ON MATCH SET c.title = $channelTitle

                    // Video Node
                    MERGE (v:Video {videoId: $videoId})
                    ON CREATE SET v.title = $videoTitle
                    ON MATCH SET v.title = $videoTitle

                    // Relationship Channel -> video
                    MERGE (c)-[:HAS_VIDEO]->(v)

                    // Comment Node
                    MERGE (cm:Comment {commentId: $commentId})
                    ON CREATE SET 
                        cm.textDisplay = $textDisplay,
                        cm.textOriginal = $textOriginal,
                        cm.category = $category
                    ON MATCH SET
                        cm.textDisplay = $textDisplay,
                        cm.textOriginal = $textOriginal,
                        cm.category = $category

                    // Relationship video -> comment
                    MERGE (v)-[:HAS_COMMENT]->(cm)
                """, {
                    "channelId": comment.video.channel.channelId,
                    "channelTitle": comment.video.channel.title,
                    "videoId": comment.video.videoId,
                    "videoTitle": comment.video.title,
                    "commentId": comment.id,
                    "textDisplay": comment.textDisplay,
                    "textOriginal": comment.textOriginal,
                    "category": comment.category
                })
        except Exception as e:
            raise Exception()

