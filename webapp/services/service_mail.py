import smtplib

from webapp.config import MAIL_USERNAME, MAIL_PASSWORD

def send_mail(sent_to_email):
    """Отправка письма пользователю с поздравление регистрации его на сайте"""

    sent_from_email = MAIL_USERNAME
    email_text = 'Hello, thank you for registering on our site.'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(sent_from_email, sent_to_email, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')