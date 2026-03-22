from core.file_operations.file_writer import write_string_temp_file
from core.graph.state import NewsPodcastState
from email_process.filtering.filter import filter_emails
from email_process.gmail.gmail import get_service, list_emails, get_email_body
from email_process.gmail.models import UnprocessedEmail

# todo handle nothing to do
def grab_emails(state: NewsPodcastState):
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

    print(f'\n👩🏻‍💻 Processing emails')
    files_path = []
    for filtered_email in filtered_emails:
        mail_content = get_email_body(service, filtered_email.message_id)
        file_path = write_string_temp_file(mail_content)
        files_path.append(file_path)

        print(f" - saved to {file_path}")

    # update the state adding
    # - all files created
    # - all files parsed (we keep them to archive them later)

    return {**state, "mail_to_process": filtered_emails, "file_to_clean": files_path}


def log_found_emails(emails: list[UnprocessedEmail]):
    for e in emails:
        print(f" - {e.from_} — {e.subject}")
