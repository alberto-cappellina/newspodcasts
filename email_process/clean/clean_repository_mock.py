from email_process.clean.clean_repository import CleanMailRepository


class CleanMailStubRepository(CleanMailRepository):
    def clean_mail_content(self, content: str) -> str:
        return content
