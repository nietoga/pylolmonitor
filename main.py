import threading
from time import sleep
import PySimpleGUIQt as sg

from mail import send_mail
from monitoring import is_lol_runing
import config

from userdata import get_user_data, set_user_data

DEFAULT_MAIL_SENDER = config.get("DEFAULT_MAIL_SENDER")


def monitor_user():
    while True:
        if is_lol_runing():
            send_mail(
                DEFAULT_MAIL_SENDER,
                get_user_data("subscriber_email"),
                "LoL Monitor Warning",
                get_user_data("name") + " is running LoL or trying to install it.",
            )

            time_to_wait_after_mail = 2 * 60 * 60  # 2 hours
            sleep(time_to_wait_after_mail)
        else:
            time_to_wait_to_check_again = 5 * 60  # 5 minutes
            sleep(time_to_wait_to_check_again)


def run_main_window():
    layout = [
        [sg.Text("Settings")],
        [sg.Text("Your Name"), sg.InputText(get_user_data("name"), key="-NAME-")],
        [
            sg.Text("Subscriber Email"),
            sg.InputText(get_user_data("subscriber_email"), key="-SUBSCRIBER_EMAIL-"),
        ],
        [sg.Button("Save"), sg.Button("Close")],
    ]

    window = sg.Window("LoL Monitor", layout)

    while True:
        event, values = window.read()

        if event == "Save":
            set_user_data("name", values["-NAME-"])
            set_user_data("subscriber_email", values["-SUBSCRIBER_EMAIL-"])
        elif event in [sg.WINDOW_CLOSED, "Close"]:
            break

    window.close()


def run_system_tray():
    tray = sg.SystemTray(menu=["", ["Open", "Exit"]], filename="rat.png")

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
