from django.forms import Form
from typing import Union
import functools

from utils.http.constants import HttpMethod, HttpStatus
from utils.http.responses.JSONResponse import JSONResponse

DEFAULT_HTTP_METHODS = {
    HttpMethod.GET: True,
    HttpMethod.POST: False,
    HttpMethod.DELETE: False,
}


def view(*, login_required=True, methods: dict[HttpMethod, bool]=DEFAULT_HTTP_METHODS, RequestForm: Form):
    allowed_http_methods = { **DEFAULT_HTTP_METHODS, **methods }

    def view_decorator(func):
        @functools.wraps(func)
        def wrapper(request):
            is_allowed_method = allowed_http_methods[request.method]
            
            if not is_allowed_method:
                return JSONResponse(error='', status=HttpStatus.METHOD_NOT_ALLOWED)
            
            if login_required and not request.user.is_authenticated:
                return JSONResponse(error='', status=HttpStatus.UNAUTHORIZED)
                
            if request.method == HttpMethod.POST:
                form = RequestForm(request.POST, request.FILES)

                if not form.is_valid():
                    return JSONResponse(error=form.errors, status=HttpStatus.BAD_REQUEST)

            return func(request)
        return wrapper
    return view_decorator