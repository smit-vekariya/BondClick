from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class MobileNumberBackend(BaseBackend):
    def authenticate(self, request, mobile=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            return None  # User with the provided mobile number does not exist
        return user

    def get_user(self, user_id):
        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None