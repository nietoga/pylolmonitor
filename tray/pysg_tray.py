import PySimpleGUIQt as sg

from tray import Tray


class SgTray(Tray):
    DOUBLE_CLICK_EVENT = sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED

    def __init__(self, icon_path: str, menu_items: list[str]) -> None:
        super().__init__(icon_path, menu_items)

        self._tray = sg.SystemTray(
            menu=["", self._menu_items],
            filename=self._icon_path,
        )

    def set_visible(self, visible):
        super().set_visible(visible)

        if self.is_visible():
            self._tray.un_hide()
        else:
            self._tray.hide()

    def close(self):
        super().close()
        self._tray.close()

    def run(self):
        while not self.is_closed():
            menu_item = self._tray.read(0)

            if menu_item in self._listeners:
                self._listeners[menu_item](self)
