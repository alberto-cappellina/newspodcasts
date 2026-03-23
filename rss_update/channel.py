from dataclasses import dataclass, field

from core.common.podcast import Podcast
from rss_update.item import Item


@dataclass
class Channel:
    title: str
    link: str
    description: str
    language: str
    author: str
    category: str
    items: list[Item] = field(default_factory=list)

    @staticmethod
    def with_podcast(podcast: Podcast) -> Channel:
        return Channel(
            title=podcast.title,
            link=podcast.link,
            description="",
            language=podcast.language,
            author=podcast.author,
            category=podcast.category,
        )
