from django.contrib import admin
from account.models import MainMenu, Company, Distributor, BondUser, State, City
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Register your models here.


@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "sequence", "url", "parent", "is_parent", "icon")


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ("is_deleted", "company", "identity_id", "name")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("is_deleted", "identity_id", "name")

# class BondUserCreationForm(UserCreationForm):
#     class Meta:
#         model = BondUser
#         fields = ('email', 'is_active', 'is_staff')

# class BondUserChangeForm(UserChangeForm):
#     class Meta:
#         model = BondUser
#         fields = ('email', 'is_active', 'is_staff')

# @admin.register(BondUser)
# class BondUserAdmin(admin.ModelAdmin):
#     form = BondUserCreationForm
#     add_form = BondUserChangeForm

#     list_display = ('email', 'is_active', 'is_staff')
#     search_fields = ('email',)

@admin.register(BondUser)
class BondUserAdmin(admin.ModelAdmin):
    list_display = ("mobile", "full_name", "address", "city", "pin_code", "state", "created_on", "company", "distributor", "is_deleted")


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("is_deleted", "code", "name")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("is_deleted", "state", "code", "name")



