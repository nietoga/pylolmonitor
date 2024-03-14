from mail import send_mail
from supervisor import is_lol_runing

if __name__ == "__main__":
    if is_lol_runing():
        send_mail()
