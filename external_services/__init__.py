from typing import Type

from mail import MailService
from user_data import UserDataProvider
from tray import Tray


class ExternalServices:
    mail_service: MailService
    user_data_provider: UserDataProvider
    Tray: Type[Tray]
