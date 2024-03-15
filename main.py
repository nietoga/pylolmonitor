from mail import send_mail
from monitoring import is_lol_runing
import config

DEFAULT_MAIL_SENDER = config.get("DEFAULT_MAIL_SENDER")

if __name__ == "__main__":
    if is_lol_runing():
        send_mail(
            DEFAULT_MAIL_SENDER,
            "agusngarci@gmail.com",
            "LoL Warning",
            "This motherfucker is trying to install LoL",
        )
