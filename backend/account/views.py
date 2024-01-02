from rest_framework.decorators import api_view
from django.http import HttpResponse
from account.models import MainMenu
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json
from rest_framework.views import APIView, View
from account.serializers import BondUserSerializers
from rest_framework_simplejwt.settings import api_settings
from datetime import datetime, timedelta
from account.models import BondUser
from django.contrib.auth import authenticate
from django.core.cache import cache
from manager import manager
from django.db.models import CharField, Value, F, Func, ExpressionWrapper
from django.shortcuts import render
from django.db.models.functions import Concat




# Create your views here.

class Welcome(View):
    template_name = "welcome.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['mobile'] = user.mobile
        return token


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
        serializer = BondUserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Registration successfully"}))
        else:
            return HttpResponse(json.dumps({"data":[], "status": 0, "message": serializer.errors}))


class RegisterBondUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self, request):
        register_user_data = request.data
        # otp = random.randint(100000, 999999)
        # send_otp_to_mobile(mobile_no, otp)
        # register_user_data["otp"] = otp
        register_user_data["otp"] = 343434
        register_user_data["otp_created"] = datetime.now()
        cache.set(register_user_data["mobile"], register_user_data)
        return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Otp has been send to mobile number successfully"}))


class VerifyRegisterUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self,request):
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
                    token = MyTokenObtainPairSerializer.get_token(user)
                    response=[{"access_token":str(token.access_token),"refresh_token":str(token)}]
                    return HttpResponse(json.dumps({"data":response, "status": 1, "message": "Registration successfully"}))
                else:
                    return HttpResponse(json.dumps({"data":[], "status": 0, "message": serializer.errors}))
            else:
                return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Your otp has been expire."}))
        return HttpResponse(json.dumps({"data":[], "status": 1, "message": "You need to registration."}))


class LoginBondUser(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self,request):
        login_data = request.data
        # otp = random.randint(100000, 999999)
        # send_otp_to_mobile(mobile_no, otp)
        # register_user_data["otp"] = otp
        login_data["otp"] = 353535
        login_data["otp_created"] = datetime.now()
        cache.set(login_data["mobile"], login_data)
        return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Otp has been send to mobile number successfully"}))


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
                    token = MyTokenObtainPairSerializer.get_token(user)
                    response=[{"access_token":str(token.access_token),"refresh_token":str(token)}]
                    return HttpResponse(json.dumps({"data":response, "status": 1, "message": "Login successfully"}))
                else:
                    return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Your otp has been expire."}))
            return HttpResponse(json.dumps({"data":[], "status": 1, "message": "You need to login with mobile number."}))
        except Exception as e:
            manager.create_from_exception(e)
            return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


class BondUserProfile(APIView):
    def get(self, request):
        try:
            user_info = BondUser.objects.filter(id=request.user.id).values("full_name","mobile","email").annotate(full_address=Concat(F("address"), Value(', '), ("pin_code"), Value(', '), F("city__name"), Value(', '), F("state__name"),output_field=CharField())).first()
            return HttpResponse(json.dumps({"data":[user_info], "status": 1, "message": "User profile details."}))
        except Exception as e:
            manager.create_from_exception(e)
            return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))

