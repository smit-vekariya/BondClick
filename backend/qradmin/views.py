from django.shortcuts import render
from account.serializers import BondUserListSerializers
from qradmin.serializers import QRBatchSerializers, QRCodeSerializers, QRBatchListSerializers, QRCodeListSerializers
from account.models import BondUser
from manager.manager import HttpsAppResponse, Util
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from qradmin.models import QRBatch, QRCode
from django.conf import settings
from django.db import transaction
from manager import manager
from rest_framework import filters
import logging
from rest_framework.pagination import PageNumberPagination
from django.db.models import Case, Count, F, Q ,When, IntegerField


# Create your views here.
class CompanyDashboard(viewsets.ViewSet):
    queryset  = QRCode.objects.all()
    user_queryset = BondUser.objects.all()

    def list(self, request):
        try:
            total_bond_user = self.user_queryset.count()
            dashboard = self.queryset.aggregate(
                total_qr_code = Count(F('id')),
                total_qr_batch = Count(F('batch'), distinct=True),
                total_used_qr = Count(Case(When(is_used=True, then=1),output_field=IntegerField())),
                total_remain_qr = Count(Case(When(is_used=False, then=1),output_field=IntegerField()))
            )
            used_in_percentage = (dashboard["total_used_qr"]) * 100 / dashboard["total_qr_code"]
            dashboard.update({"used_in_percentage":round(used_in_percentage,2)})
            dashboard.update({"total_bond_user":total_bond_user})
            return HttpsAppResponse.send(dashboard, 0, "Dashboard data get successfully")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param= "page_size"
    max_page_size = 1000

class UserList(generics.ListAPIView):
    queryset = BondUser.objects.all()
    filter_backends = [filters.OrderingFilter]
    serializer_class = BondUserListSerializers
    pagination_class = CustomPagination

class QRBatchList(generics.ListAPIView):
    queryset = QRBatch.objects.all()
    filter_backends = [filters.OrderingFilter]
    serializer_class = QRBatchListSerializers
    pagination_class = CustomPagination

class QRCodeList(generics.ListAPIView):
    queryset = QRCode.objects.all()
    filter_backends = [filters.OrderingFilter]
    serializer_class = QRCodeListSerializers
    pagination_class = CustomPagination
import time
class CreateQRBatch(APIView):
    def post(self, request):
        try:
            with transaction.atomic():
                data = request.data
                total_qr_code = data.get("total_qr_code")
                point_per_qr = data.get("point_per_qr")
                if point_per_qr > 0 and total_qr_code > 0:
                    batch_number = QRBatch.objects.values("batch_number").last()
                    batch_number = "BATCH-10000" if not batch_number else f"BATCH-{int(batch_number['batch_number'].split('-')[1])+1}"
                    point_per_amount = data.get("point_per_amount")
                    total_point = data.get("total_point")
                    total_amount = data.get("total_amount")
                    amount_per_qr = data.get("amount_per_qr")

                    batch_data={"batch_number":batch_number,"total_qr_code":total_qr_code,"total_amount":total_amount,
                                "point_per_amount":point_per_amount,"total_point":total_point,"point_per_qr":point_per_qr,
                                "amount_per_qr":amount_per_qr,"created_by_id":request.user,"expire_on":None}

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
                    return HttpsAppResponse.send([], 0, "Total QR Code and Point Per QR must be grater then 0.")
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


# class CreateQRBatch(APIView):
#     def get(self, request):
#         try:
#             with transaction.atomic():
#                 data = request.data
#                 total_qr_code = data.get("quantity",None)
#                 point_per_qr = data.get("point_per_qr",None)
#                 if point_per_qr > 0 and total_qr_code > 0:
#                     batch_number = QRBatch.objects.values("batch_number").last()
#                     batch_number = "BATCH-10000" if not batch_number else f"BATCH-{int(batch_number['batch_number'].split('-')[1])+1}"
#                     point_per_amount = int(settings.POINT_PER_AMOUNT)
#                     total_point = total_qr_code * point_per_qr
#                     total_amount = total_point / point_per_amount
#                     amount_per_qr = total_amount / total_qr_code

#                     batch_data={"batch_number":batch_number,"total_qr_code":total_qr_code,"total_amount":total_amount,
#                                 "point_per_amount":point_per_amount,"total_point":total_point,"point_per_qr":point_per_qr,
#                                 "amount_per_qr":amount_per_qr,"created_by_id":request.user,"expire_on":None}

#                     serializer = QRBatchSerializers(data=batch_data)
#                     if serializer.is_valid():
#                         is_created = CreateQRCode.create_qr_code(batch_number,total_qr_code,point_per_qr)
#                         if is_created:
#                             qr_serializer = QRCodeSerializers(data=is_created, many=True)
#                             if qr_serializer.is_valid():
#                                 serializer.save()
#                                 qr_serializer.save()
#                                 return HttpsAppResponse.send([], 1, "QR Batch has been create successfully.")
#                             else:
#                                 return HttpsAppResponse.send([], 0, qr_serializer.errors)
#                         else:
#                             return HttpsAppResponse.send([], 0, "Something went wrong when create qr code")
#                     else:
#                         return HttpsAppResponse.send([], 0, serializer.errors)
#                 else:
#                     return HttpsAppResponse.send([], 0, "Amount and quantity must be grater then 0.")
#         except Exception as e:
#             return HttpsAppResponse.exception(str(e))