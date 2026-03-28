from typing import TypedDict

from core.common.podcast_job import PodcastJob
from core.configuration.config import Config


class NewsPodcastState(TypedDict):
    # this field will hold the configuration
    config: Config

    # this field will hold the mails to be processed
    jobs_list: list[PodcastJob]
