import threading
import pystray
from pystray import MenuItem as item
from PIL import Image


def open_window(icon: pystray.Icon) -> None:
    print("Opening Window...")
    # COMPLEX STUFF INVOLVING PYSIMPLEGUI


def notify_observer(icon: pystray.Icon) -> None:
    if icon.HAS_NOTIFICATION:
        icon.notify("YOU HAVE BEEN CAUGHT")
    # COMPLEX STUFF INVOLVING SENDING EMAIL


def setup(icon: pystray.Icon) -> None:
    icon.visible = True

    while not exit_event.is_set():
        print("OBSERVING AND VALIDATING")
        exit_event.wait(5 * 60)


def close_tray(icon: pystray.Icon) -> None:
    icon.visible = False
    exit_event.set()
    icon.stop()


icon = "rat.png"
image = Image.open(icon)

menu = pystray.Menu(
    item("Show", open_window, default=True),
    item("Notify", notify_observer),
    item("Quit", close_tray),
)

exit_event = threading.Event()

trayIcon = pystray.Icon("pylolnotifier", image, "LoL Notifier", menu)
trayIcon.run_detached(setup)
