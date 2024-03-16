import threading
from time import sleep
import PySimpleGUIQt as sg

from mail import send_mail
from monitoring import is_lol_runing
import config

DEFAULT_MAIL_SENDER = config.get("DEFAULT_MAIL_SENDER")


def monitor_user():
    while True:
        if is_lol_runing():
            send_mail(
                DEFAULT_MAIL_SENDER,
                "agusngarci@gmail.com",
                "LoL Warning",
                "This motherfucker is trying to install LoL",
            )

        sleep(5)


def run_main_window():
    layout = [[sg.Text("Settings")], [sg.Button("Save"), sg.Button("Close")]]

    window = sg.Window("LoL Notifier", layout)

    while True:
        event, _ = window.read()

        if event in [sg.WINDOW_CLOSED, "Close"]:
            break

    window.close()


def run_system_tray():
    tray = sg.SystemTray(menu=["", ["Open", "Exit"]], filename="rat.png")
    tray.ShowMessage("LoL Notifier", "We're up and running! Don't mess it up")

    while True:
        menu_item = tray.read()

        if menu_item == "Exit":
            break
        elif menu_item in [sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED, "Open"]:
            tray.hide()
            run_main_window()
            tray.un_hide()

    tray.close()


if __name__ == "__main__":
    lol_monitor_thread = threading.Thread(target=monitor_user, daemon=True)
    lol_monitor_thread.start()
    run_system_tray()
