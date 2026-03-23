import logging

from core.configuration.config import Config
from email_process.gmail.models import UnprocessedEmail

logger = logging.getLogger(__name__)


def filter_emails(emails: list[UnprocessedEmail], config: Config) -> list[UnprocessedEmail]:
    """Filter emails against configured items.

    An email is included if it matches at least one item in config.items.
    Matching requires both conditions to be true:

    - sender_match: every string in item.filter.sender is a case-insensitive
      substring of the email's From address (AND logic across the list).
    - title_match: item.filter.title is a case-insensitive substring of the
      email's subject (empty title always matches).

    Each email is appended at most once (first matching item wins).
    """
    result = []
    for email in emails:
        for podcast_config in config.podcasts_config:
            sender_match = all(s.lower() in (email.from_ or "").lower() for s in podcast_config.filter.sender)
            title_match = podcast_config.filter.title.lower() in (email.subject or "").lower()
            if sender_match and title_match:
                logger.info(
                    "Email matched podcast '%s': from='%s' subject='%s'",
                    podcast_config.podcast.id,
                    email.from_,
                    email.subject,
                )
                email.matching_podcast = podcast_config.podcast
                result.append(email)
                break
    return result
