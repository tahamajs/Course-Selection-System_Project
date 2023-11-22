from django.core.mail import EmailMessage
from django.conf import settings


def send_email(subject, body, to):
    EmailMessage(from_email=settings.EMAIL_SENDER, subject=subject, body=body, to=[to, ]).send()

    
if not settings.DEBUG:
    import celery

    send_email = celery.shared_task()(send_email)

    
def send_password_reset_email(link, to):
    body = 'Hi, \nUse link below to reset your password \n' + link
    subject = 'Reset Your Password'

    if settings.DEBUG:
        send_email(subject, body, to)
    else:
        send_email.delay(subject, body, to)
