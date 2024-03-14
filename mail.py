import config

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

SENDGRID_API_KEY = config.get("SENDGRID_API_KEY")
SENDGRID_FROM_EMAIL = config.get("SENDGRID_FROM_EMAIL")

print(SENDGRID_API_KEY, type(SENDGRID_API_KEY))
print(SENDGRID_FROM_EMAIL, type(SENDGRID_FROM_EMAIL))

subscriber_email = "agusngarci@gmail.com"


def build_mail() -> Mail:
    from_email = Email(SENDGRID_FROM_EMAIL)
    to_email = To(subscriber_email)
    subject = Subject("LoL Monitor Alert")
    plain_text_content = PlainTextContent("This motherfucker is installing LoL")
    html_content = HtmlContent("<strong>This motherfucker is running LoL</strong>")
    mail = Mail(from_email, to_email, subject, plain_text_content, html_content)
    return mail


def _get_sendgrid_api_client() -> SendGridAPIClient:
    return SendGridAPIClient(api_key=SENDGRID_API_KEY)


def send_mail() -> None:
    sg = _get_sendgrid_api_client()
    mail = build_mail()
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
