import os

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def get_absolute_path(local_path: str) -> str:
    return os.path.join(CURRENT_DIRECTORY, local_path)
