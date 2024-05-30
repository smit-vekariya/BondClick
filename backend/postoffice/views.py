from django.shortcuts import render
import json
import requests
from django.conf import settings
import logging
import random
from manager.manager import HttpsAppResponse,create_from_exception
from django.db import transaction

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


def send_mail_delay(receiver, subject, message, cc=None, bcc=None):
    try:
        with transaction.atomic():
            sender = settings.EMAIL_HOST_USER
            EmailLog.objects.create(mail_from=sender, mail_to=receiver, subject=subject, message=message, mail_cc=cc, mail_bcc=bcc, status="pending")
            return HttpsAppResponse.send([], 1, "Send mail successfully.")
    except Exception as e:
        return HttpsAppResponse.exception(str(e))

def send_email_task(id):
    try:
        pass
    except Exception as e:
        return "Failed to send mail."

# def send_mail_now(receiver, subject, message, cc=None, bcc=None):
#     try:
#         with transaction.atomic():
#             sender = settings.EMAIL_HOST_USER
#             EmailLog.objects.create(mail_from=sender, mail_to=receiver, subject=subject, message=message,mail_cc=cc, mail_bcc=bcc)
#             return HttpsAppResponse.send([], 1, "Send mail successfully.")
#     except Exception as e:
#         return HttpsAppResponse.exception(str(e))