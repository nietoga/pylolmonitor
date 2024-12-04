from mailjet_rest import Client

from mail import MailService


class MailJetService(MailService):
    def __init__(self, api_key: str, api_secret: str, debug: bool = False) -> None:
        super().__init__()
        self._mailjet_client = Client(auth=(api_key, api_secret), version="v3.1")
        self._debug = debug

    def send_mail(
        self,
        email_from: str,
        email_to: str,
        subject: str,
        text_part: str,
        html_part: str | None = None,
    ) -> bool:
        data = {
            "Messages": [
                {
                    "From": {"Email": email_from},
                    "To": [{"Email": email_to}],
                    "Subject": subject,
                    "TextPart": text_part,
                    "HTMLPart": html_part,
                }
            ]
        }

        response = self._mailjet_client.send.create(data=data)

        if self._debug:
            print(response.status_code)
            print(response.json())

        return response.ok
