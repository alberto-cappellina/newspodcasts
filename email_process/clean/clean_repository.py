from abc import ABC, abstractmethod


class CleanMailRepository(ABC):
    @abstractmethod
    def clean_mail_content(self, content: str) -> str:
        pass
