from django.shortcuts import render
import json
import requests
from django.conf import settings
import logging
from manager.manager import HttpsAppResponse

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