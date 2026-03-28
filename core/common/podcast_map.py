from dataclasses import dataclass, field

from core.common.podcast_job import PodcastJob
from email_process.gmail.models import UnprocessedEmail


@dataclass
class PodcastMap:
    jobs: dict[str, PodcastJob] = field(default_factory=dict)

    def jobs_list(self) -> list[PodcastJob]:
        return list(self.jobs.values())

    def add_email_to_podcast(self, email: UnprocessedEmail) -> None:
        podcast = email.matching_podcast
        if podcast is None:
            return
        if podcast.id in self.jobs:
            self.jobs[podcast.id].emails.append(email)
        else:
            self.jobs[podcast.id] = PodcastJob(podcast=podcast, emails=[email])
