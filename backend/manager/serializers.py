from rest_framework import serializers
from manager.models import SystemParameter
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule, ClockedSchedule

class SystemParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemParameter
        fields = '__all__'

    # def create(self, validate):
    #     SystemParameter.objects.create(*validate)


class IntervalScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = '__all__'


class CrontabScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = '__all__'


class ClockedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockedSchedule
        fields = '__all__'


class PeriodicTaskSerializer(serializers.ModelSerializer):
    scheduler = serializers.SerializerMethodField()
    expires = serializers.SerializerMethodField()
    last_run_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    date_changed = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    
    class Meta:
        model = PeriodicTask
        fields = ["id","name","task","enabled","expires","start_time","last_run_at","total_run_count","date_changed","scheduler"]

    def get_scheduler(self,objects):
        if objects.interval:
            return str(objects.interval)
        if objects.crontab:
            return str(objects.crontab.human_readable)
        if objects.clocked:
            return str(objects.clocked)
        
    def get_expires(self,objects):
        if objects.expires:
            return str(objects.expires)
        elif objects.expire_seconds:
            return str(objects.expire_seconds) +" seconds"
        else:
            return None