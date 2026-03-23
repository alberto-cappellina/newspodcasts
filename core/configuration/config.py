from dataclasses import dataclass, field

from core.common.podcast import Podcast


@dataclass
class Config:
    feed_url: str
    base_url: str
    username: str
    password: str
    podcasts_config: list["PodcastConfig"] = field(default_factory=list)


@dataclass
class FilterConfig:
    sender: list[str] = field(default_factory=list)
    title: str = ""


@dataclass
class PodcastConfig:
    podcast: Podcast
    filter: FilterConfig = field(default_factory=FilterConfig)
