from abc import ABC, abstractmethod


class MailService(ABC):
    @abstractmethod
    def send_mail(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        text_part: str,
        html_part: str | None = None,
    ) -> bool:
        return False
