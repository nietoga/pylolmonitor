import threading
from time import sleep
import PySimpleGUIQt as sg

from monitoring import is_lol_runing
import config

import file_utils

from external_services import ExternalServices
import external_services.configuration as external_services_config

external_services_config.configure()
mail_service = ExternalServices.mail_service
user_data = ExternalServices.user_data_provider
Tray = ExternalServices.Tray

DEFAULT_MAIL_SENDER = config.get("DEFAULT_MAIL_SENDER")


def monitor_user():
    while True:
        if is_lol_runing():
            subscriber_email = user_data.get_user_data("subscriber_email")
            name = user_data.get_user_data("name", "Someone")
            email_sent = False

            if subscriber_email:
                email_sent = mail_service.send_mail(
                    DEFAULT_MAIL_SENDER,
                    subscriber_email,
                    "LoL Monitor Warning",
                    name + " is running LoL or trying to install it.",
                )

            if email_sent:
                time_to_wait_after_mail_success = 2 * 60 * 60  # 2 hours
                sleep(time_to_wait_after_mail_success)
            else:
                print("Couldn't send email.")
                time_to_wait_after_mail_failure = 10 * 60  # 10 minutes
                sleep(time_to_wait_after_mail_failure)
        else:
            time_to_wait_to_check_again = 5 * 60  # 5 minutes
            sleep(time_to_wait_to_check_again)


def run_main_window():
    layout = [
        [sg.Text("Settings")],
        [
            sg.Text("Your Name"),
            sg.InputText(user_data.get_user_data("name", ""), key="-NAME-"),
        ],
        [
            sg.Text("Subscriber Email"),
            sg.InputText(
                user_data.get_user_data("subscriber_email", ""),
                key="-SUBSCRIBER_EMAIL-",
            ),
        ],
        [sg.Button("Save"), sg.Button("Close")],
    ]

    window = sg.Window(
        "LoL Monitor",
        layout,
        size=(300, 1),
        icon=file_utils.get_absolute_path("rat.ico"),
    )

    while True:
        event, values = window.read()

        if event == "Save":
            user_data.set_user_data("name", values["-NAME-"])
            user_data.set_user_data("subscriber_email", values["-SUBSCRIBER_EMAIL-"])
        elif event in [sg.WINDOW_CLOSED, "Close"]:
            break

    window.close()


def run_system_tray():
    def close_tray(tray: Tray):
        tray.close()

    def open_window(tray: Tray):
        tray.set_visible(False)
        run_main_window()
        tray.set_visible(True)

    tray = Tray(file_utils.get_absolute_path("rat.ico"), ["Open", "Exit"])
    tray.attach_listener("Exit", close_tray)
    tray.attach_listener("Open", open_window)
    tray.attach_listener(Tray.DOUBLE_CLICK_EVENT, open_window)
    tray.run()


def exit_application(signum, frame):
    exit()


def main():
    import signal

    signal.signal(signal.SIGINT, exit_application)
    signal.signal(signal.SIGTERM, exit_application)

    lol_monitor_thread = threading.Thread(target=monitor_user, daemon=True)
    lol_monitor_thread.start()
    run_system_tray()


if __name__ == "__main__":
    main()
