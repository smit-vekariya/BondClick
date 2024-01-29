from rest_framework import serializers
from qradmin.models import QRCode, QRBatch


class QRBatchSerializers(serializers.ModelSerializer):
    class Meta:
        model= QRBatch
        fields = '__all__'

        # def create(self, validated_data):
            # return super().create(*validated_data)


class QRCodeSerializers(serializers.ModelSerializer):
    batch__batch_number = serializers.CharField()

    class Meta:
        model = QRCode
        fields = ["qr_number", "qr_code", "point", "batch__batch_number"]

    def create(self, validated_data):
        validated_data["batch"] = QRBatch.objects.get(batch_number=validated_data["batch__batch_number"])
        validated_data.pop("batch__batch_number")
        QRCode.objects.create(**validated_data)
