from celery import shared_task
from django.core.mail import send_mail
import time

@shared_task(bind=True)
def send_email_fun(self,subject, message, sender, receiver):
    # time.sleep(5) # for check that sending email process runs in background 
    send_mail(subject, message, sender, [receiver])

