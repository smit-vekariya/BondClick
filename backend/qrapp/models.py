from django.db import models
from account.models import BondUser
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import transaction
from django.db.models import F
# Create your models here.


class BondUserWallet(models.Model):
    user = models.ForeignKey(BondUser, on_delete=models.CASCADE)
    point = models.IntegerField(default=0, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    withdraw_point = models.IntegerField(default=0, null=True, blank=True)
    withdraw_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)


    def __str__(self):
        return str(self.user)


transaction_types = (("credit","Credit"), ("debit","Debit"))
class Transaction(models.Model):
    wallet =models.ForeignKey(BondUserWallet, on_delete=models.PROTECT)
    description = models.TextField()
    tran_type = models.CharField(max_length=100, choices=transaction_types)
    point = models.IntegerField(null=True, blank=True,default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tran_on = models.DateTimeField(auto_now=True)
    tran_by = models.ForeignKey(BondUser, on_delete=models.PROTECT)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.pk is None:
            point_per_amount = int(settings.POINT_PER_AMOUNT)
            amount = self.point / point_per_amount
            if self.tran_type == "credit":
                self.wallet.balance = F('balance') + amount
                self.wallet.point = F('point') + self.point
            if self.tran_type == "debit":
                self.wallet.balance = F('balance') - amount
                self.wallet.point = F('point') - self.point
                self.wallet.withdraw_balance = F('withdraw_balance') + amount
                self.wallet.withdraw_point = F('withdraw_point') + self.point
            self.amount = amount
            self.wallet.save()
            super(Transaction, self).save(*args, **kwargs)
        else:
            print('Update is not possible after transaction')


wallet_action_types = (
    ("credit_point", "Credit Point"),
    ("debit_point", "Debit Point"),
    ("w_money", "Withdraw Money"),
    ("error", "Error")
)

class WalletHistory(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id =  models.IntegerField(null=True, blank=True)
    action = models.TextField()
    action_type = models.CharField(max_length=100, choices=wallet_action_types, null=True, blank=True)
    ip_addr = models.CharField(default="", max_length=45)
    action_on = models.DateTimeField(auto_now=True)
    action_by = models.ForeignKey(BondUser, on_delete=models.PROTECT)