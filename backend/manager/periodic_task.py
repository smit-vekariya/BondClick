from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule, ClockedSchedule
from manager.manager import HttpsAppResponse
import json
from rest_framework import viewsets
from datetime import datetime, timedelta
from celery import shared_task
from rest_framework.response import Response
from manager.manager import Util
from manager.serializers import PeriodicTaskSerializer

# https://django-celery-beat.readthedocs.io/en/latest/    

class CreateScheduler(viewsets.ViewSet):
    permission_classes =[]
    authentication_classes =[]

    def create_scheduler(self, request):
        try:
            schedule_type = request.POST["type"]
            if schedule_type == "interval" : 
                return self.create_interval_scheduler(request, request.POST)
            elif schedule_type == "crontab" : 
                return self.create_crontab_scheduler(request, request.POST)
            elif schedule_type == "clocked" : 
                return self.create_clocked_scheduler(request, request.POST)
            else:
                return HttpsAppResponse.send([], 0, "Invalid schedule type.")
        except  Exception as e:
            return HttpsAppResponse.exception(str(e))


    def create_interval_scheduler(self, request, data):
        try:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=data["every"],
                period=data["period"] #dropdown
            )
            if schedule:
                PeriodicTask.objects.create(
                    interval=schedule,   
                    name=data["name"],
                    task=data["task"], # dropdown
                    args=json.dumps(json.loads(data["args"])),
                    # expire_seconds =10,
                    # kwargs=json.dumps({
                    #     'be_careful': True,
                    # }),
                    # expires=datetime.strptime(data["expires"], '%Y-%m-%d %H:%M:%S.%f') if data["expires"] else None
                    # expires= datetime.now()  + timedelta(seconds=60)
                )
                return HttpsAppResponse.send([], 1, "Periodic task created successfully.")
            else:
                return HttpsAppResponse.send([], 0, "Something wrong with interval scheduler.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


    def create_crontab_scheduler(self, request, data):
        try:
            schedule, created = CrontabSchedule.objects.get_or_create(
                minute=data["minute"],
                hour=data["hour"], 
                day_of_week=data["day_of_week"], #0 for Sunday
                day_of_month=data["day_of_month"],
                month_of_year=data["month_of_year"],
            )
            if schedule:
                PeriodicTask.objects.create(
                    crontab=schedule,   
                    name=data["name"],
                    task=data["task"],
                    args=json.dumps(json.loads(data["args"])),
                )
                return HttpsAppResponse.send([], 1, "Periodic task created successfully.")
            else:
                return HttpsAppResponse.send([], 0, "Something wrong with crontab scheduler.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))
    
    def create_clocked_scheduler(self, request, data):
        try:
            schedule, created = ClockedSchedule.objects.get_or_create(
                clocked_time=data["clocked_time"],
            )
            if schedule:
                PeriodicTask.objects.create(
                    clocked=schedule,   
                    name=data["name"],
                    task=data["task"],
                    one_off=True,
                    args=json.dumps(json.loads(data["args"])),
                )
                return HttpsAppResponse.send([], 1, "Periodic task created successfully.")
            else:
                return HttpsAppResponse.send([], 0, "Something wrong with cloked scheduler.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))
    
    

@shared_task(name="test", bind=True)
def test(self):
    print("=====> this is for testing <========")


# note:

# 1. stop scheduler if any error occure 
# OR
# 2. run scheduler and skip task for that time where error occure dont stop task 
# stop calling task after expire


class PeriodicTaskView(viewsets.ModelViewSet):
    permission_classes =[]
    authentication_classes =[]
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return HttpsAppResponse.send(serializer.data, 1, "Periodic task listed successfully.")
