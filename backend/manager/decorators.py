from functools import wraps
from manager.manager import has_permission
from manager.manager import HttpsAppResponse


def has_perm(act_code):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(self, request, *args, **kwargs):
            if has_permission(self.request.user, act_code) is False:
                return HttpsAppResponse.send([], 0, "You don't have permission to perform this action.")
            return view(self, request, *args, **kwargs)
        return _wrapped_view
    return decorator

# All Example : https://www.w3resource.com/python-exercises/decorator/index.php

#Example: check secret key in header
# def check_secret_key(function):
#     @wraps(function)
#     def decorator(request, *args, **kwrgs):
#         key = request.headers.get("Secret-Key")
#         if key == settings.SECRET_KEY:
#             return function(request, *args, **kwrgs)
#         else:
#         return HttpResponse(json.dumps({"data":{}, "status": 0, "message": "Secret key did not match!"}))

#     return decorator
