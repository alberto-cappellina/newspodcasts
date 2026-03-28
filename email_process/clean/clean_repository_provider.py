from core.common import constants
from email_process.clean.clean_repository import CleanMailRepository
from email_process.clean.clean_repository_mock import CleanMailStubRepository
from email_process.clean.clean_repository_with_llm import CleanMailLlmRepository


def provide_clean_repository() -> CleanMailRepository:
    if constants.use_clean_stub:
        return CleanMailStubRepository()

    return CleanMailLlmRepository()
