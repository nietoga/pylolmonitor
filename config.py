from dotenv import dotenv_values

_config = dotenv_values(".env")


def get(key: str) -> str | None:
    return _config.get(key)
