import config
from mail.mailjet import MailJetService

MAILJET_API_KEY = config.get("MAILJET_API_KEY")
MAILJET_API_SECRET = config.get("MAILJET_API_SECRET")

mail_service = MailJetService(
    api_key=MAILJET_API_KEY,
    api_secret=MAILJET_API_SECRET,
)
