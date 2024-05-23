from functools import wraps
from manager.manager import Util
from manager.manager import HttpsAppResponse

def has_perm(act_code):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(self, request, *args, **kwargs):
            if Util.has_perm(self.request.user, act_code) is False:
                return HttpsAppResponse.send([], 0, "You don't have permission to perform this action.")
            return view(self, request, *args, **kwargs)
        return _wrapped_view
    return decorator


# def check_secret_key(function):
#     @wraps(function)
#     def decorator(request, *args, **kwrgs):
#         key = request.headers.get("Secret-Key")
#         if key == settings.SECRET_KEY:
#             return function(request, *args, **kwrgs)
#         else:
#         return HttpResponse(json.dumps({"data":{}, "status": 0, "message": "Secret key did not match!"}))

#     return decorator
