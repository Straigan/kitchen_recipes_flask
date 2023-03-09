from smtplib import SMTPRecipientsRefused, SMTP_SSL
from typing import Dict

from loguru import logger

from webapp.celery_app import celery
from webapp.config import MAIL_PASSWORD, MAIL_USERNAME

from wtforms import FileField


@celery.task
def send_mail(params_send_email: Dict[str, FileField]) -> None:
    """Отправка письма пользователю с поздравление регистрации его на сайте"""

    send_from_email = MAIL_USERNAME
    send_to_email = params_send_email['send_to_email']
    email_text = 'Hello, thank you for registering on our site.'
    server = SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(MAIL_USERNAME, MAIL_PASSWORD)
    try:
        server.sendmail(send_from_email, send_to_email, email_text)
        info_send_email = f"Письмо отправлено {send_to_email}"
        logger.info(info_send_email)
    except SMTPRecipientsRefused:
        logger.error("Письмо не отправлено")

    server.close()
    print('Email send!')
