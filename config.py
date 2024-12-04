from dotenv import dotenv_values
import file_utils

_config = dotenv_values(file_utils.get_absolute_path(".env"))


def get(key: str) -> str | None:
    return _config.get(key)
