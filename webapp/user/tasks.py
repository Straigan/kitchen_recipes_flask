from smtplib import SMTPRecipientsRefused, SMTP_SSL
from typing import Dict

from webapp.celery_app import celery
from webapp.config import MAIL_PASSWORD, MAIL_USERNAME

from wtforms import FileField


@celery.task
def send_mail(params_send_email: Dict[str, FileField]) -> None:
    """Отправка письма пользователю с поздравление регистрации его на сайте"""

    send_from_email = MAIL_USERNAME
    email_text = 'Hello, thank you for registering on our site.'
    server = SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(MAIL_USERNAME, MAIL_PASSWORD)

    try:
        server.sendmail(send_from_email, params_send_email['send_to_email'], email_text)
    except SMTPRecipientsRefused:
        print('Something went wrong...')

    server.close()
    print('Email send!')
