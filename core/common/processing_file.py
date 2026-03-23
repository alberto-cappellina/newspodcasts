from dataclasses import dataclass

from core.common.podcast import Podcast


@dataclass
class ProcessingFile:
    path: str
    podcast: Podcast
