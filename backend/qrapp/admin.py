from django.contrib import admin
from qrapp.models import BondUserWallet

# Register your models here.
@admin.register(BondUserWallet)
class MainMenuBondUserWallet(admin.ModelAdmin):
    list_display = ("user","point","balance","withdraw_point","withdraw_balance")