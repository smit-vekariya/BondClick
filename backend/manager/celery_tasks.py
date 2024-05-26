from celery import shared_task
from django.core.mail import send_mail
import time
import os 


@shared_task(serializer='json', name="send_mail")
def send_email_fun(subject, message, sender, receiver):
    print(subject)
    # time.sleep(20) # for check that sending email process runs in background 
    send_mail(subject, message, sender, [receiver])


send_email_fun("test","test","panelprime.dev@gmail.com","smit.intellial@gmail.com")