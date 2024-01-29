from django.db import models
from account.models import BondUser

# Create your models here.

class QRBatch(models.Model):
    batch_number = models.CharField(unique=True, max_length=20)
    total_qr_code = models.IntegerField(null=True, blank=True)
    total_used_qr_code = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    point_per_amount = models.IntegerField(null=True, blank=True)
    total_point = models.IntegerField(null=True, blank=True)
    point_per_qr = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(BondUser, on_delete=models.CASCADE, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_printed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    expire_on = models.DateTimeField(null=True, blank=True)
    is_used= models.BooleanField(default=False)

    def __str__(self):
        return str(self.batch_number)


class QRCode(models.Model):
    qr_number = models.CharField(unique=True, max_length=20)
    qr_code = models.CharField(unique=True, max_length=50)
    batch = models.ForeignKey(QRBatch, on_delete=models.PROTECT)
    point = models.IntegerField(null=True, blank=True)
    used_on = models.DateTimeField(null=True, blank=True)
    used_by = models.ForeignKey(BondUser, on_delete=models.CASCADE, null=True, blank=True)
    is_printed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_used= models.BooleanField(default=False)

    def __str__(self):
        return str(self.qr_number)

