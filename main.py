from mail import send_mail
from supervisor import is_lol_runing

if __name__ == "__main__":
    if is_lol_runing():
        send_mail(
            "agusnieto.gg@gmail.com",
            "agusngarci@gmail.com",
            "LoL Warning",
            "This motherfucker is trying to install LoL",
        )
