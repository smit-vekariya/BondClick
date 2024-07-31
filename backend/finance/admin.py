from django.contrib import admin
from finance.models import FinUser, Transactions
# Register your models here.


@admin.register(FinUser)
class FinUserAdmin(admin.ModelAdmin):
    list_display= ('name',)

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display= ('fin_user','amount','is_income')
    
