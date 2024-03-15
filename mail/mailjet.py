from mailjet_rest import Client
import config

MAILJET_API_KEY = config.get("MAILJET_API_KEY")
MAILJET_API_SECRET = config.get("MAILJET_API_SECRET")

mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version="v3.1")


def send_mail(
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

    response = mailjet.send.create(data=data)

    print(response.status_code)
    print(response.json())

    return response.ok
