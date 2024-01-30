from django.shortcuts import render
from rest_framework.views import APIView, View
from manager.manager import HttpsAppResponse, Util
from manager import manager
from account.models import BondUser
from qradmin.models import QRBatch, QRCode
from qrapp.models import BondUserWallet, Transaction
from datetime import datetime
from django.db import transaction
from django.db.models import F, Q


# Create your views here.

class ScanQRCode(APIView):
    def get(self, request):
        try:
            with transaction.atomic():
                data = request.data
                mobile = data["mobile"]
                qr_code = data["qrcode"]
                user_id = request.user.id
                point = 0
                if data:
                    if BondUser.objects.filter(mobile=mobile, id=user_id).exists():
                        qr_details= QRCode.objects.filter(qr_code=qr_code, is_deleted=False, batch__is_deleted=False).all().first()
                        if qr_details:
                            if not qr_details.is_used:
                                point = qr_details.point
                                qr_details.is_used = True
                                qr_details.used_on = datetime.now()
                                qr_details.used_by_id = user_id
                                qr_details.save()
                                wallet_id = BondUserWallet.objects.filter(user_id=user_id).values("id").first()
                                Transaction.objects.create(wallet_id=wallet_id["id"], description=f"Scan '{qr_code}'", tran_type="credit", point=point, tran_by_id=user_id)
                                msg = f"Congratulations on successfully scanning the QR Code! You've earned {point} points. Well done!"
                            else:
                                msg = "This token has been used."
                        else:
                            msg = "This token not found."
                        return HttpsAppResponse.send([{"Point":point}], 1, msg)
                    else:
                        return HttpsAppResponse.send([], 0, "User Does not match.")
                return HttpsAppResponse.send([], 0, "QRCode data not found.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))


