import config

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

SENDGRID_API_KEY = config.get("SENDGRID_API_KEY")
SENDGRID_FROM_EMAIL = config.get("SENDGRID_FROM_EMAIL")


sendgrid_client = SendGridAPIClient(api_key=SENDGRID_API_KEY)


def send_mail(
    email_from: str,
    email_to: str,
    subject: str,
    text_part: str,
    html_part: str | None = None,
) -> bool:
    mail = Mail(
        Email(email_from),
        To(email_to),
        Subject(subject),
        PlainTextContent(text_part),
        HtmlContent(html_part) if html_part else None,
    )

    response = sendgrid_client.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)

    return 200 <= response.status_code < 300
