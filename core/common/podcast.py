from dataclasses import dataclass


@dataclass
class Podcast:
    id: str
    title: str
    link: str
    language: str
    author: str
    category: str
