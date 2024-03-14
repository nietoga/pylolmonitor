from dotenv import dotenv_values

_config = dotenv_values(".env")


def get(key):
    return _config.get(key)
