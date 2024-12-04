import config
from mail.mailjet import MailJetService

MAILJET_API_KEY = config.get("MAILJET_API_KEY") or ""
MAILJET_API_SECRET = config.get("MAILJET_API_SECRET") or ""

mail_service = MailJetService(
    api_key=MAILJET_API_KEY,
    api_secret=MAILJET_API_SECRET,
)
