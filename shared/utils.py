from django.core.mail import EmailMessage
from django.conf import settings


# import celery


# @celery.shared_task()
def send_email(subject, body, to):
    return EmailMessage(from_email=settings.EMAIL_SENDER, subject=subject, body=body, to=[to, ])#.send()


def send_password_reset_email(link, to):
    body = 'Hi, \nUse link below to reset your password \n' + link
    subject = 'Reset Your Password'
    send_email(subject, body, to)
