from rest_framework import serializers
from qrapp.models import  BondUserWallet, Transaction


class BondUserWalletSerializers(serializers.ModelSerializer):
    class Meta:
        model = BondUserWallet
        fields = "__all__"

        # def create(self, validate):
        #     BondUserWallet.objects.create(*validate)


class TransactionSerializers(serializers.ModelSerializer):
    tran_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Transaction
        fields= ["description","tran_type","point","amount","tran_on"]