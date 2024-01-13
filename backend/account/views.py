from django.http import HttpResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json
from rest_framework.views import APIView, View
from account.serializers import BondUserSerializers
from datetime import datetime, timedelta
from account.models import BondUser
from django.contrib.auth import authenticate
from django.core.cache import cache
from manager import manager
from manager.manager import HttpsAppResponse
from django.db.models import CharField, Value, F
from django.shortcuts import render
from django.db.models.functions import Concat
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from account.models import MainMenu,UserToken, City, State


# Create your views here.

class Welcome(View):
    template_name = "welcome.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        try:
            token = super().get_token(user)
            token['mobile'] = user.mobile
            access_token =  str(token.access_token)
            refresh_token = str(token)
            UserToken.objects.update_or_create(user_id=user.id,defaults={'access_token': access_token})
            update_last_login(None, user)
            response=[{"access_token":str(access_token),"refresh_token":refresh_token}]
            return response
        except Exception as e:
            manager.create_from_exception(e)



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MainMenuView(APIView):
    authentication_classes =[]
    permission_classes = []
    def get(self, request):
        menu = list(MainMenu.objects.values().order_by("sequence"))
        return HttpResponse(json.dumps(menu))


class RegisterUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self, request):
        try:
            serializer = BondUserSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return HttpsAppResponse.send([], 1, "Registration successfully")
            else:
                return HttpsAppResponse.send([], 0, serializer.errors)
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


class RegisterBondUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self, request):
        try:
            register_user_data = request.data
            # otp = random.randint(100000, 999999)
            # send_otp_to_mobile(mobile_no, otp)
            # register_user_data["otp"] = otp
            register_user_data["otp"] = 343434
            register_user_data["otp_created"] = datetime.now()
            cache.set(register_user_data["mobile"], register_user_data)
            return HttpsAppResponse.send([], 1, "Otp has been send to mobile number successfully")
        except Exception as e:
           return HttpsAppResponse.exception(str(e))


class VerifyRegisterUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self,request):
        try:
            verify_data = request.data
            user_data = cache.get(verify_data["mobile"])
            if user_data:
                current_time = datetime.now()
                opt_validate = current_time - user_data["otp_created"]
                if opt_validate < timedelta(minutes=1):
                    user_data["company"] = 1
                    serializer = BondUserSerializers(data=user_data)
                    if serializer.is_valid():
                        serializer.save()
                        user = authenticate(request, mobile=user_data["mobile"])
                        tokens = MyTokenObtainPairSerializer.get_token(user)
                        return HttpsAppResponse.send(tokens, 1, "Registration successfully")
                    else:
                        return HttpsAppResponse.send([], 0, serializer.errors)
                else:
                    return HttpsAppResponse.send([], 1, "Your otp has been expire.")
            return HttpsAppResponse.send([], 1, "You need to registration.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


class LoginBondUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self,request):
        try:
            login_data = request.data
            # otp = random.randint(100000, 999999)
            # send_otp_to_mobile(mobile_no, otp)
            # register_user_data["otp"] = otp
            login_data["otp"] = 353535
            is_exit=  BondUser.objects.filter(mobile=login_data["mobile"]).exists()
            if is_exit:
                login_data["otp_created"] = datetime.now()
                cache.set(login_data["mobile"], login_data)
                return HttpsAppResponse.send([], 1, "Otp has been send to mobile number successfully")
            else:
                return HttpsAppResponse.send([], 1, "User not found.")
        except Exception as e:
           return HttpsAppResponse.exception(str(e))


class VerifyLoginBondUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self,request):
        try:
            login_data = request.data
            user_data = cache.get(login_data["mobile"])
            if user_data:
                current_time = datetime.now()
                opt_validate = current_time - user_data["otp_created"]
                if opt_validate < timedelta(minutes=1):
                    user = authenticate(request, mobile=login_data["mobile"])
                    tokens = MyTokenObtainPairSerializer.get_token(user)
                    return HttpsAppResponse.send(tokens, 1, "Login successfully")
                else:
                    return HttpsAppResponse.send([], 1, "Your otp has been expire.")
            return HttpsAppResponse.send([], 1, "You need to login with mobile number.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


class LogoutBondUser(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            UserToken.objects.filter(user_id=request.user.id).delete()
            token = RefreshToken(token=refresh_token)
            token.blacklist()
            return HttpsAppResponse.send([], 1, "User logout successfully.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


class BondUserProfile(APIView):
    def get(self, request):
        try:
            user_info = BondUser.objects.filter(id=request.user.id).values("full_name","mobile").annotate(full_address=Concat(F("address"), Value(', '), ("pin_code"), Value(', '), F("city__name"), Value(', '), F("state__name"),output_field=CharField())).first()
            return HttpsAppResponse.send([user_info], 1, "User profile details.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


class GetCityState(APIView):
    def get(self,request):
        try:
            city = list(City.objects.filter(is_deleted=False).values("id","name").order_by("name"))
            state = list(State.objects.filter(is_deleted=False).values("id","name").order_by("name"))
            response = [{"City":city,"State":state}]
            return HttpsAppResponse.send(response, 1, "City and state data fetch successfully.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))