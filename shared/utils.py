from django.core.mail import EmailMessage
from django.conf import settings


def create_email(subject, body, to):
    return EmailMessage(from_email=settings.EMAIL_SENDER, subject=subject, body=body, to=[to, ])


def send_password_reset_email(link, to):
    body = 'Hi, \nUse link below to reset your password \n' + link
    subject = 'Reset Your Password'
    create_email(subject, body, to).send()
