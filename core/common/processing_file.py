from dataclasses import dataclass

from core.common.podcast import Podcast
from email_process.gmail.models import UnprocessedEmail


@dataclass
class ProcessingFile:
    path: str
    podcast: Podcast
    email: UnprocessedEmail

    def to_file_to_convert(self, file_to_convert_path):
        pass
