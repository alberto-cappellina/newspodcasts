from typing import TypedDict

from core.configuration.config import Config
from email_process.gmail.models import UnprocessedEmail


class NewsPodcastState(TypedDict):
    # this field will hold the configuration
    config: Config

    # this field will hold the mails to be processed
    mail_to_process: list[UnprocessedEmail]

    # this field will hold the list of files to be cleaned
    file_to_clean: list[str]

    # this field will hold the list of files to be converted
    file_to_converted: list[str]
