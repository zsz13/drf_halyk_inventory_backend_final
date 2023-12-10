from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from inventory.models import InventoryItem


@shared_task
def send_email_notification():
    thirty_minutes_ago = timezone.now() - timezone.timedelta(minutes=1)
    new_entries = InventoryItem.objects.filter(time_create__gte=thirty_minutes_ago)

    if new_entries.exists():
        subject = 'Уведомление: Добавлены новые записи'
        message = 'Были добавлены новые записи в системе инвентаризации.'
        from_email = 'your_email@example.com'  # Замените на ваш электронный адрес
        recipient_list = ['danyar.ismailov@gmail.com']  # Замените на адреса получателей

        send_mail(subject, message, from_email, recipient_list)
    else:
        subject = 'Уведомление: Не добавлены новые записи'
        message = 'Не были добавлены новые записи в системе инвентаризации.'
        from_email = 'your_email@example.com'  # Замените на ваш электронный адрес
        recipient_list = ['danyar.ismailov@gmail.com']  # Замените на адреса получателей

        send_mail(subject, message, from_email, recipient_list)


