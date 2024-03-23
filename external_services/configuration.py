from external_services import ExternalServices


def _configure_mail():
    from .mail import mail_service

    ExternalServices.mail_service = mail_service


def configure():
    _configure_mail()
