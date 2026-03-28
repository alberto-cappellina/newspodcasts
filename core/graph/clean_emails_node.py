from core.common.podcast_job import PodcastJob
from core.file_operations.file_writer import read_file, write_string_temp_file
from core.graph import NewsPodcastState
from email_process.clean.clean_repository import CleanMailRepository
from email_process.clean.clean_repository_provider import provide_clean_repository


def clean_files_for_job(job: PodcastJob):
    clean_repository: CleanMailRepository = provide_clean_repository()

    for file in job.file_to_clean:
        print(f" - load file{file.path}")
        file_content = read_file(file.path)

        clean_content = clean_repository.clean_mail_content(file_content)
        cleaned_file_path = write_string_temp_file(clean_content)
        print(f"   > clean file wrote to {cleaned_file_path}")

        processing_file = file.to_file_to_convert(file_to_convert_path=cleaned_file_path)

        job.file_to_convert.append(processing_file)



def clean_emails(state: NewsPodcastState) -> dict:
    print(f"\n🧹 Cleaning files")

    jobs_list: list[PodcastJob] = state["jobs_list"]

    for job in jobs_list:
        clean_files_for_job(job)

    return {**state}



