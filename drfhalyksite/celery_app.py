import os
from datetime import timedelta

from celery import Celery
from django.conf import settings
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfhalyksite.settings')

app = Celery('drfhalyksite')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'send_daily_statistics': {
        'task': 'inventory.tasks.send_daily_statistics',
        'schedule': timedelta(days=1),
    },
}
