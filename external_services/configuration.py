from external_services import ExternalServices


def _configure_mail():
    from .mail import mail_service

    ExternalServices.mail_service = mail_service


def _configure_user_data():
    from .user_data import user_data_provider

    ExternalServices.user_data_provider = user_data_provider


def configure():
    _configure_mail()
    _configure_user_data()
