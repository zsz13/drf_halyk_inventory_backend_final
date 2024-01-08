from datetime import timedelta, datetime
from smtplib import SMTPServerDisconnected
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from inventory.models import InventoryItem


@shared_task
def send_email_task(subject, message, recipient_list):
    try:
        send_mail(subject, message, 'osvobozdennyjdzango37@gmail.com', recipient_list)
    except SMTPServerDisconnected as e:
        print(f"SMTPServerDisconnected error: {e}")


@shared_task
def send_daily_statistics():
    # hourly statistics beat
    # now = datetime.now(timezone.utc)
    # start_time = datetime(now.year, now.month, now.day, 10, 13, 0, tzinfo=timezone.utc)
    # end_time = datetime(now.year, now.month, now.day, 10, 50, 0, tzinfo=timezone.utc)
    # new_entries = InventoryItem.objects.filter(time_create__gte=start_time, time_create__lt=end_time).count()
    # statistics_message = (
    #     f'Statistics for {start_time.strftime("%d-%m-%Y %H:%M:%S %z")} to {end_time.strftime("%d-%m-%Y %H:%M:%S %z")}:\n'
    #     f'New entries: {new_entries}\n'
    # )

    today = timezone.now()
    yesterday = today - timedelta(days=1)
    new_entries = InventoryItem.objects.filter(time_create__gte=yesterday, time_create__lt=today).count()
    statistics_message = (
        f'Statistics for {yesterday.strftime("%d-%m-%Y")} to {today.strftime("%d-%m-%Y")}:\n'
        f'New entries: {new_entries}\n'
    )
    subject = 'Daily Statistics'
    recipient_list = ['danyar.ismailov@gmail.com']
    send_mail(subject, statistics_message, 'osvobozdennyjdzango37@gmail.com', recipient_list)
