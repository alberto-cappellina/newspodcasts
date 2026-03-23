from dataclasses import dataclass

from core.common.podcast import Podcast


@dataclass
class UnprocessedEmail:
    message_id: str
    from_: str
    subject: str
    matching_podcast: Podcast | None
