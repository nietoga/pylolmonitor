import PySimpleGUIQt as sg

from user_data import UserDataProvider


class SgUserDataProvider(UserDataProvider):
    def __init__(self, settings_prefix: str = "") -> None:
        super().__init__()
        self._settings_prefix = settings_prefix

    def set_user_data(self, key: str, value: str) -> None:
        sg.user_settings_set_entry(self._settings_prefix + key, value)

    def get_user_data(self, key: str, default: str | None = None) -> str | None:
        return sg.user_settings_get_entry(self._settings_prefix + key, default)
