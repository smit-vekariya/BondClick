from django.shortcuts import render
from account.serializers import BondUserListSerializers
from qradmin.serializers import QRBatchSerializers, QRCodeSerializers
from account.models import BondUser
from manager.manager import HttpsAppResponse, Util
from rest_framework import generics
from rest_framework.views import APIView
from qradmin.models import QRBatch, QRCode
from django.conf import settings
from django.db import transaction
from manager import manager
from rest_framework import filters
import logging
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param= "page_size"
    max_page_size = 1000


class UserList(generics.ListAPIView):
    authentication_classes =[]
    permission_classes = []
    queryset = BondUser.objects.all()
    filter_backends = [filters.OrderingFilter]
    serializer_class = BondUserListSerializers
    pagination_class = CustomPagination



class CreateQRBatch(APIView):
    def get(self, request):
        try:
            with transaction.atomic():
                data = request.data
                total_qr_code = data.get("quantity",None)
                total_amount = data.get("amount",None)
                if total_amount > 0 and total_qr_code > 0:
                    batch_number = QRBatch.objects.values("batch_number").last()
                    batch_number = "BATCH-10000" if not batch_number else f"BATCH-{int(batch_number['batch_number'].split('-')[1])+1}"
                    point_per_amount = settings.POINT_PER_AMOUNT
                    total_point = point_per_amount * total_amount
                    point_per_qr = total_point / total_qr_code

                    batch_data={"batch_number":batch_number,"total_qr_code":total_qr_code,"total_amount":total_amount,
                                "point_per_amount":point_per_amount,"total_point":total_point,"point_per_qr":point_per_qr,
                                "created_by_id":request.user,"expire_on":None}

                    serializer = QRBatchSerializers(data=batch_data)
                    if serializer.is_valid():
                        is_created = CreateQRCode.create_qr_code(batch_number,total_qr_code,point_per_qr)
                        if is_created:
                            qr_serializer = QRCodeSerializers(data=is_created, many=True)
                            if qr_serializer.is_valid():
                                serializer.save()
                                qr_serializer.save()
                                return HttpsAppResponse.send([], 1, "QR Batch has been create successfully.")
                            else:
                                return HttpsAppResponse.send([], 0, qr_serializer.errors)
                        else:
                            return HttpsAppResponse.send([], 0, "Something went wrong when create qr code")
                    else:
                        return HttpsAppResponse.send([], 0, serializer.errors)
                else:
                    return HttpsAppResponse.send([], 0, "Amount and quantity must be grater then 0.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


class CreateQRCode(APIView):
    def create_qr_code(batch_number, quantity, point_per_qr):
        try:
            batch_number_ = batch_number.split('-')[1]
            bulk_qr = []
            qr_number_next = 10000
            for qty in range(quantity):
                qr_code = Util.create_unique_qr_code(batch_number_)
                qr_number_with_batch = f"QR-{batch_number_}-{qr_number_next}"
                bulk_qr.append({"qr_number":qr_number_with_batch,"qr_code":qr_code,"batch__batch_number":batch_number,"point":point_per_qr})
                qr_number_next = qr_number_next + 1
            return bulk_qr
        except Exception as e:
            logging.exception("Something went wrong.")
            manager.create_from_exception(e)
            return False
