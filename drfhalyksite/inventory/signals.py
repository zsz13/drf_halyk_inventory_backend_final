from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from inventory.tasks import send_email_task
from inventory.models import InventoryItem


@receiver(post_save, sender=InventoryItem)
def send_email_on_new_entry(sender, instance, created, **kwargs):
    if created:
        subject = 'New record added'
        formatted_time = instance.time_create.strftime('%d-%m-%Y %H:%M:%S %z').replace("+0000", "by UTC+0:00")
        message = f'A new record with ID: {instance.id} has been added. Created at {formatted_time}'

    else:
        subject = 'An existing record has been updated'
        formatted_time = instance.time_update.strftime('%d-%m-%Y %H:%M:%S %z').replace("+0000", "by UTC+0:00")
        message = f'Record with ID: {instance.id} has been updated. Updated at {formatted_time}'
    recipient_list = ['danyar.ismailov@gmail.com']
    send_email_task.delay(subject, message, recipient_list)


@receiver(post_delete, sender=InventoryItem)
def send_email_on_delete(sender, instance, **kwargs):
    subject = 'Record Deleted'
    formatted_time = timezone.localtime().strftime('%d-%m-%Y %H:%M:%S %z').replace("+0600", "by UTC+6:00")
    message = f'Record with ID: {instance.id} has been deleted at {formatted_time}'
    recipient_list = ['danyar.ismailov@gmail.com']
    send_email_task.delay(subject, message, recipient_list)
