import PySimpleGUIQt as sg


def set_user_data(key: str, value: str) -> None:
    sg.user_settings_set_entry(key, value)


def get_user_data(key: str, default: str | None = None) -> str | None:
    return sg.user_settings_get_entry(key, default)
