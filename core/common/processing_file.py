from dataclasses import dataclass


@dataclass
class ProcessingFile:
    path: str
    podcast_id: str
