import datetime
import json
import logging
import math
import random
import pytz
import requests
import sys
import uuid
import traceback as traceback_mod
import warnings

from dateutil import tz
from django.conf import settings
from django.core.cache import cache
from django.db import connection
from django.http import HttpResponse
from django.utils.encoding import smart_str
from manager.models import ErrorBase


def create_from_exception(self, url=None, exception=None, traceback=None, **kwargs):
    if not exception:
        exc_type, exc_value, traceback = sys.exc_info()
    elif not traceback:
        warnings.warn("Using just the ``exception`` argument is deprecated, send ``traceback`` in addition.", DeprecationWarning)
        exc_type, exc_value, traceback = sys.exc_info()
    else:
        exc_type = exception.__class__
        exc_value = exception

    def to_unicode(f):
        if isinstance(f, dict):
            nf = dict()
            for k, v in f.items():
                nf[str(k)] = to_unicode(v)
            f = nf
        elif isinstance(f, (list, tuple)):
            f = [to_unicode(f) for f in f]
        else:
            try:
                f = smart_str(f)
            except (UnicodeEncodeError, UnicodeDecodeError):
                f = "(Error decoding value)"
        return f

    tb_message = "\n".join(traceback_mod.format_exception(exc_type, exc_value, traceback))

    kwargs.setdefault("message", to_unicode(exc_value))
    level = logging.ERROR
    if kwargs.get("level"):
        level = kwargs["level"]

    ErrorBase.objects.create(class_name=exc_type.__name__, message=to_unicode(exc_value), traceback=tb_message, level=level)


def create_from_text(message, class_name=None, level=40, traceback=None):
    ErrorBase.objects.create(class_name=class_name, message=message, traceback=traceback, level=level)


class HttpsAppResponse:
    def send(data,status,message):
        return HttpResponse(json.dumps({"data":data, "status": status, "message": message}))

    def exception(error):
        logging.exception("Something went wrong.")
        create_from_exception(error)
        return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(error)}))


class Util(object):

    @staticmethod
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
            # return 343434
        except Exception as e:
            logging.exception("Something went wrong.")
            create_from_exception(e)
            return 0

    @staticmethod
    def create_unique_qr_code(batch_number):
        uuid_code = str(uuid.uuid4())
        uuid_upper = uuid_code.replace("-","")
        qr_code = f"QR-{batch_number}-{uuid_upper.upper()}"
        return qr_code

    @staticmethod
    def set_cache(schemas, key, value, time=3600):
        schemas_key = schemas + key
        cache.set(schemas_key, value, time)

    @staticmethod
    def get_cache(schemas, key):
        schemas_key = schemas + key
        if schemas_key in cache:
            return cache.get(schemas_key)
        return None

    @staticmethod
    def clear_cache(schemas, key):
        schemas_key = schemas + key
        if schemas_key in cache:
            cache.delete(schemas_key)
            
    @staticmethod
    def get_local_time(utctime, showtime=False, time_format=None):
        if utctime == "" or utctime is None or utctime == 0 or utctime == "-":
            return ""
        timezone_info = Util.get_timezone_info()
        from_zone = tz.gettz("UTC")
        to_zone = tz.gettz(timezone_info)
        utctime = utctime.replace(tzinfo=from_zone)
        new_time = utctime.astimezone(to_zone)
        if showtime:
            if time_format is None:
                time_format = "%d/%m/%Y %H:%M"
            return new_time.strftime(time_format)
        else:
            return new_time.strftime("%d/%m/%Y")
        
    @staticmethod
    def convert_time_to_utc(timeobj, time_format=None):
        local_timezone = Util.get_timezone_info()
        timezone = pytz.timezone(local_timezone)
        local_time = timezone.localize(timeobj)
        to_zone = tz.gettz("UTC")
        if time_format is None:
            time_format = "%d/%m/%Y %H:%M"
        utc_time = local_time.astimezone(to_zone).strftime(time_format)
        return utc_time

    @staticmethod
    def get_utc_datetime(local_datetime, has_time, timezone):
        naive_datetime = None
        local_time = pytz.timezone(timezone)

        if has_time:
            naive_datetime = datetime.datetime.strptime(local_datetime, "%d/%m/%Y %H:%M")
        else:
            naive_datetime = datetime.datetime.strptime(local_datetime, "%d/%m/%Y")

        local_datetime = local_time.localize(naive_datetime, is_dst=None)
        utc_datetime = local_datetime.astimezone(pytz.utc)
        return utc_datetime
    
    @staticmethod
    def get_human_readable_time(minutes):
        time = ""
        cal_hrs = int(minutes / 60)
        days = int(cal_hrs / 24)
        hrs = cal_hrs - days * 24
        mins = int(minutes - (cal_hrs * 60))
        secs = int((minutes - mins - (hrs * 60) - (days * 24 * 60)) * 60)

        if days != 0:
            days = "%02d" % (days)
            time += str(days) + "d"
            if hrs != 0 or mins != 0 or secs != 0:
                time += ":"
        if hrs != 0:
            spent_hours = "%02d" % (hrs)
            time += str(spent_hours) + "h"
            if mins != 0 or secs != 0:
                time += ":"
        if mins != 0:
            mins = "%02d" % round(mins)
            time += str(mins) + "m"
            if secs != 0:
                time += ":"
        if secs != 0:
            secs = "%02d" % round(secs)
            time += str(secs) + "s"
        return time
    
# def check_secret_key(function):
#     @wraps(function)
#     def decorator(request, *args, **kwrgs):
#         key = request.headers.get("Secret-Key")
#         if key == settings.SECRET_KEY:
#             return function(request, *args, **kwrgs)
#         else:
#         return HttpResponse(json.dumps({"data":{}, "status": 0, "message": "Secret key did not match!"}))

#     return decorator