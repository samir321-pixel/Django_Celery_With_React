from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sending_Mail_Using_Celery.settings')

app = Celery('Sending_Mail_Using_Celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'every-60-seconds': {
        'task': 'mail_app.tasks.send_mails',
        'schedule': 60,
    },
}
app.autodiscover_tasks()
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.conf.timezone = 'UTC'
