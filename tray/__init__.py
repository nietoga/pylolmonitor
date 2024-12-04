from abc import ABC, abstractmethod


class Tray(ABC):
    DOUBLE_CLICK_EVENT = "__DOUBLE_CLICK__"

    def __init__(self, icon_path: str, menu_items: list[str]) -> None:
        self._icon_path = icon_path
        self._menu_items = menu_items
        self._visible = True
        self._closed = False
        self._listeners: dict[str,] = {}

    def set_visible(self, visible):
        self._visible = visible

    def is_visible(self):
        return self._visible

    def close(self):
        self._closed = True

    def is_closed(self):
        return self._closed

    def attach_listener(self, key, listener):
        self._listeners[key] = listener

    @abstractmethod
    def run():
        pass
