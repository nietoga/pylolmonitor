from external_services import ExternalServices


def _configure_mail():
    from .mail import mail_service

    ExternalServices.mail_service = mail_service


def _configure_user_data():
    from .user_data import user_data_provider

    ExternalServices.user_data_provider = user_data_provider


def _configure_tray_class():
    from .tray import TrayClass

    ExternalServices.Tray = TrayClass


def configure():
    _configure_mail()
    _configure_user_data()
    _configure_tray_class()
