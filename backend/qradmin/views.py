from django.shortcuts import render
from account.serializers import BondUserSerializers
from manager import manager
from account.models import BondUser
from manager.manager import HttpsAppResponse, Util
from rest_framework import generics

# Create your views here.

class UserList(generics.ListAPIView):
    authentication_classes =[]
    permission_classes = []
    queryset = BondUser.objects.all()
    serializer_class = BondUserSerializers
