from dataclasses import dataclass


@dataclass
class UnprocessedEmail:
    message_id: str
    from_: str
    subject: str
    matching_podcast_id: str | None
