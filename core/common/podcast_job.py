from dataclasses import dataclass, field

from core.common.podcast import Podcast
from core.common.processing_file import ProcessingFile
from email_process.gmail.models import UnprocessedEmail


@dataclass
class PodcastJob:
    podcast: Podcast
    emails: list[UnprocessedEmail] = field(default_factory=list)
    file_to_clean: list[ProcessingFile] = field(default_factory=list)
    file_to_convert: list[ProcessingFile] = field(default_factory=list)
    file_mp3: list[ProcessingFile] = field(default_factory=list)
