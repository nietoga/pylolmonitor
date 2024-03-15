import pystray
from pystray import MenuItem as item
from PIL import Image


def open_window(icon, query):
    print("Opening Window...")
    # COMPLEX STUFF INVOLVING PYSIMPLEGUI


def notify_observer(icon):
    if icon.HAS_NOTIFICATION:
        icon.notify("YOU HAVE BEEN CAUGHT")
    # COMPLEX STUFF INVOLVING SENDING EMAIL


def close_tray(icon):
    icon.stop()


icon = "rat.png"
image = Image.open(icon)

menu = pystray.Menu(
    item("Show", open_window, default=True),
    item("Notify", notify_observer),
    item("Quit", close_tray),
)

trayIcon = pystray.Icon("pylolnotifier", image, "LoL Notifier", menu)
trayIcon.run()
