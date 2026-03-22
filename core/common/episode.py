from dataclasses import dataclass
from datetime import datetime


@dataclass
class Episode:
    title: str
    description: str
    link: str
    pubDate: datetime
    episode: int
    duration: str
    url: str
    length: int
    type: str
    guid: str
