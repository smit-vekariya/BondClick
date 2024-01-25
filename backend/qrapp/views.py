from django.shortcuts import render
from rest_framework.views import APIView, View
from manager.manager import HttpsAppResponse, Util
from manager import manager

# Create your views here.

class ScanQRCode(APIView):
    def get(self, request):
        try:
            data = request.data
            if data:
                Point = 20
                return HttpsAppResponse.send([{"Point":Point}], 1, f"Congratulations on successfully scanning the QR Code! You've earned {Point} points. Well done!")
            return HttpsAppResponse.send([], 0, "QRCode data not found.")
        except Exception as e:
            manager.create_from_exception(e)
