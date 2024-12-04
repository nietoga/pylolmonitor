from abc import ABC, abstractmethod


class UserDataProvider(ABC):
    @abstractmethod
    def set_user_data(self, key: str, value: str) -> None:
        pass

    @abstractmethod
    def get_user_data(self, key: str, default: str | None = None) -> str | None:
        pass
