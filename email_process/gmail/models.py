from dataclasses import dataclass
from datetime import datetime

from core.common.podcast import Podcast


@dataclass
class UnprocessedEmail:
    message_id: str
    from_: str
    subject: str
    received_at: datetime | None
    matching_podcast: Podcast | None
