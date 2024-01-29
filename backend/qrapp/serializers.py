from rest_framework import serializers
from qrapp.models import QRCode, QRBatch, BondUserWallet


class BondUserWalletSerializers(serializers.ModelSerializer):
    class Meta:
        model = BondUserWallet
        fields = "__all__"

        # def create(self, validate):
        #     BondUserWallet.objects.create(*validate)