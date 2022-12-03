from django.forms import Form
import functools

from utils.http.constants import HttpMethod, HttpStatus
from utils.http.responses.JSONResponse import JSONResponse

def view(*, RequestForm: Form):
    def view_decorator(func):
        @functools.wraps(func)
        def wrapper(request):
            if request.method == HttpMethod.POST:
                form = RequestForm(request.POST, request.FILES)

                if not form.is_valid():
                    return JSONResponse({ 'errors': form.errors }, status=HttpStatus.BAD_REQUEST)

            return func(request)
        return wrapper
    return view_decorator