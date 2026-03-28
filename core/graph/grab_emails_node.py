from core.common.podcast_job import PodcastJob
from core.common.podcast_map import PodcastMap
from core.common.processing_file import ProcessingFile
from core.file_operations.file_writer import write_string_temp_file
from core.graph.state import NewsPodcastState
from email_process.filtering.filter import filter_emails
from email_process.gmail.gmail import get_service, list_emails, get_email_body
from email_process.gmail.models import UnprocessedEmail


def process_emails(podcast_job: PodcastJob, service):
    print(f'\n👩🏻‍💻 Processing emails')

    for filtered_email in podcast_job.emails:
        mail_content = get_email_body(service, filtered_email.message_id)
        file_path = write_string_temp_file(mail_content)

        file = ProcessingFile(
            path=file_path,
            podcast=filtered_email.matching_podcast,
            email=filtered_email
        )

        podcast_job.file_to_clean.append(file)

        print(f" - saved to {file_path} for {podcast_job.podcast.title}")


def grab_emails(state: NewsPodcastState) -> dict:
    service = get_service()
    configuration = state["config"]

    # get the email in found in inbox
    print(f'\n📩 Getting email')
    emails = list_emails(service, max_results=25)
    log_found_emails(emails)

    # filter the email
    print(f'\n🌪️ Filtering emails')
    filtered_emails = filter_emails(emails, configuration)
    log_found_emails(filtered_emails)

    #
    podcast_map = PodcastMap()
    for email in filtered_emails:
        # attach email to relative podcast
        podcast_map.add_email_to_podcast(email=email)

    for podcast_job in podcast_map.jobs_list():
        process_emails(podcast_job, service)

    updated_jobs = podcast_map.jobs_list()

    return {**state, "updated_jobs": updated_jobs}


def log_found_emails(emails: list[UnprocessedEmail]) -> None:
    for e in emails:
        print(f" - {e.from_} — {e.subject}")
