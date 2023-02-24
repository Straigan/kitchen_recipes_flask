import smtplib

from webapp.config import MAIL_USERNAME, MAIL_PASSWORD
from webapp.celery_app import celery

@celery.task
def send_mail(params_send_email):
    """Отправка письма пользователю с поздравление регистрации его на сайте"""

    send_from_email = MAIL_USERNAME
    email_text = 'Hello, thank you for registering on our site.'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(send_from_email, params_send_email['send_to_email'], email_text)
        server.close()

        print('Email send!')
    except:
        print('Something went wrong...')