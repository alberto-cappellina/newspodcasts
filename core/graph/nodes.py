from enum import Enum


class GraphNode(Enum):
    GRAB_EMAILS = "grab_emails"
    CLEAN_EMAILS = "clean_emails"
    CONVERT_TEXT_FILES = "convert_text_to_mp3"
    PUBLISH_MP3 = "publish_mp3"
