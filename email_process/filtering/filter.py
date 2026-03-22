from core.configuration.config import Config
from email_process.gmail.models import UnprocessedEmail


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
        for item in config.items:
            sender_match = all(s.lower() in (email.from_ or "").lower() for s in item.filter.sender)
            title_match = item.filter.title.lower() in (email.subject or "").lower()
            if sender_match and title_match:
                result.append(email)
                break
    return result
