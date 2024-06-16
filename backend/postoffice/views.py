from django.shortcuts import render
import json
from django.views import View
import requests
from django.conf import settings
import logging
import random
from manager.manager import HttpsAppResponse,create_from_exception,create_from_text
from django.db import transaction
from postoffice.models import EmailLog
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.views import APIView
from django.utils import timezone
from postoffice.serializers import EmailLogSerializer

# for multiple receiver add comma sepreter
# SendMail.send_mail(request.user, True, "smit.intellial@gmail.com","this is subject","this is body")

class SendMail(APIView):
    
    def post(self, request):
        try:
            mail = request.data["mail_data"]
            send_mail =  self.send_mail(request.user, True, mail["to"], mail["subject"], mail["body"])
            if send_mail:
                return HttpsAppResponse.send([], 1, "Mail send Successfully.")
            else:
                return HttpsAppResponse.send([], 0, "Something went wrong.")
        except Exception as e:
            return HttpsAppResponse.exception(str(e))

    # send_mail on save model method using signals
    @staticmethod
    def send_mail(action_by, is_now, receiver, subject, message, cc=None, bcc=None):
        try:
            with transaction.atomic():
                sender = settings.EMAIL_HOST_USER
                action_by = action_by if action_by.id else None
                serializer = EmailLogSerializer(data={'mail_from': sender, 'mail_to': receiver, 'subject': subject, 'message': message, 'mail_cc': cc, 'mail_bcc': bcc, 'status':'pending', 'action_by_id':action_by.id, 'is_now':is_now})
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise Exception(str(serializer.errors))
                return True
        except Exception as e:
            create_from_exception(e)
            logging.exception("Something went wrong.")
            return False

    @staticmethod
    def send_mail_now(mail_id):
        mail = EmailLog.objects.get(id=mail_id)
        try:
            sender = mail.mail_from
            receiver = (mail.mail_to).split(',')
            subject = mail.subject
            message = mail.message
            send_mail(subject, message, sender, receiver, fail_silently=True)
            mail.status = 'sent'
        except Exception as e:
            mail.status = 'failed'
            mail.error_message = str(e)
            create_from_exception(e)
        mail.updated_at = timezone.now()
        mail.save()


#Mobile number is fix (contact green api for more: https://greenapi.com/en/docs/api)
def send_whatsapp_message(message):
    try:
        url=settings.GREEN_API
        payload={
                    "chatId": "9537127284@c.us", 
                    "message": message,
                }
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
        print(response.text.encode('utf8'))
    except Exception  as e:
      return HttpsAppResponse.exception(str(e))


def send_otp_to_mobile(mobile_no):
    try:
        if mobile_no:
            otp = random.randint(100000, 999999)
            url = settings.FAST2SMS
            api_key =  settings.FAST2SMS_API_KEY
            querystring = {"authorization":api_key,"variables_values":str(otp),"route":"otp","numbers":mobile_no}
            headers = { 'cache-control': "no-cache" }
            response = requests.request("GET", url, headers=headers, params=querystring)
            response = json.loads(response.text)
            if response["return"]:
                return otp
            else:
                create_from_text("Error in OTP sending", "Important", 10, f"response => {response}, info => mobile: '{mobile_no}' otp: '{otp}'")
                if response["status_code"] == 995:
                    return "Sending multiple sms to same number is not allowed. Please try again later."
                else:
                    return "We encountered an issue while sending the OTP. Please try again later."
        else:
            return "We encountered an issue while sending the OTP. Please try again later."
    except Exception as e:
        logging.exception("Something went wrong.")
        create_from_exception(e)
        return 0

