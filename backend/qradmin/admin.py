from django.contrib import admin
from qradmin.models import QRCode, QRBatch

# Register your models here.

@admin.register(QRCode)
class MainMenuQRCode(admin.ModelAdmin):
    list_display = ("qr_number","batch","point","qr_code","is_used","used_by")


@admin.register(QRBatch)
class MainMenuQRBatch(admin.ModelAdmin):
    list_display = ("batch_number","total_amount", "total_point","point_per_amount", "point_per_qr")