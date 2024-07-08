from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule, ClockedSchedule
from manager.manager import HttpsAppResponse
import json
from datetime import datetime, timedelta

# https://django-celery-beat.readthedocs.io/en/latest/


def interval_schedule(request):
    try:
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        if created:
            return HttpsAppResponse.send([], 1, "Interval scheduler created successfully.")
        else:
            return HttpsAppResponse.send([], 1, "Interval scheduler already created.")
    except Exception as e:
        return HttpsAppResponse.exception(str(e))
    
    
def crontab_schedule(request):
    try:
        schedule, created = CrontabSchedule.objects.get_or_create(
            minute='1',
            hour='*',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )
        if created:
            return HttpsAppResponse.send([], 1, "Crontab scheduler created successfully.")
        else:
            return HttpsAppResponse.send([], 1, "Crontab scheduler already created.")
    except Exception as e:
        return HttpsAppResponse.exception(str(e))
    
    
def periodic_task(request):
    try:
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,   
            name='Send mail 1',
            task='postoffice.views.send_mail_schedule',
            args=json.dumps([105]),
            # expires=datetime.now() + timedelta(seconds=30)
        )
        return HttpsAppResponse.send([], 1, "Periodic task created successfully.")
    except Exception as e:
        return HttpsAppResponse.exception(str(e))
    