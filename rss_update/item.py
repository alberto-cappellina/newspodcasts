import uuid
from dataclasses import dataclass
from datetime import datetime

from core.common.podcast import Podcast


@dataclass
class Item:
    title: str
    description: str
    link: str
    pub_date: datetime
    episode: int
    episode_type: str
    duration: str
    enclosure: str
    guid: str

    @staticmethod
    def with_podcast(podcast: Podcast, episode: int, duration_seconds: int, mp3: str) -> Item:
        return Item(
            title=podcast.title,
            description="",
            link=podcast.link,
            pub_date=datetime.now(),
            episode=episode,
            episode_type="full",
            duration=str(duration_seconds),
            enclosure=mp3,
            guid=str(uuid.uuid4()),
        )
