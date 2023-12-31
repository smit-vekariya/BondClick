from rest_framework import serializers
from account.models import BondUser


# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields= '__all__'

#     def create(self, validate):
#         user =User(email=validate["email"],
#                    username=validate["username"],
#                    first_name=validate["first_name"],
#                    last_name=validate["last_name"])
#         user.set_password(validate["password"])
#         user.save()
#         return User


class BondUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = BondUser
        fields = '__all__'

        def create(self, validate):
            print(validate,"=====================")
            BondUser.objects.create(*validate)