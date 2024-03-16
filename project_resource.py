import os

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def get_path(path: str) -> str:
    return os.path.join(CURRENT_DIRECTORY, path)
