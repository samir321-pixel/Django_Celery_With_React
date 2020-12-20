from celery import Celery, shared_task
from .models import User_mail
from django.core.mail import send_mail

app = Celery('tasks', broker='redis://localhost:6379/')


@shared_task
def send_mails():
    for user in User_mail.objects.all():
        subject = user.subject
        message = '{}.'.format(user.message)
        email = user.email
        try:
            send_mail(subject, message, email, [email])
        except Exception as e:
            print(e)
