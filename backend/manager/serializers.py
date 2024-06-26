from rest_framework import serializers
from manager.models import SystemParameter


class SystemParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemParameter
        fields = '__all__'

    # def create(self, validate):
    #     SystemParameter.objects.create(*validate)