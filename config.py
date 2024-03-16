from dotenv import dotenv_values
import project_resource

_config = dotenv_values(project_resource.get_path(".env"))


def get(key: str) -> str | None:
    return _config.get(key)
