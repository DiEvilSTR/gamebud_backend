from django.forms import Form
from django.http import QueryDict
from django.http.multipartparser import MultiPartParser
import functools

from utils.http.constants import HttpMethod, HttpStatus
from utils.http.responses.JSONResponse import JSONResponse
from utils.http.responses.JSONResponse import JSONResponse


# TODO: Change everything
def view(*, login_required=True, delete:Form=None, get:Form=None, patch:Form=None, post:Form=None, put:Form=None):
    methods_forms = {
        HttpMethod.DELETE: delete,
        HttpMethod.GET: get,
        HttpMethod.PATCH: patch,
        HttpMethod.POST: post,
        HttpMethod.PUT: put,
    }

    def view_decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            ValidationForm = methods_forms.get(request.method)

            if not ValidationForm or not issubclass(ValidationForm, Form):
                return JSONResponse(error='', status=HttpStatus.METHOD_NOT_ALLOWED)

            if login_required and not request.user.is_authenticated:
                return JSONResponse(error='', status=HttpStatus.UNAUTHORIZED)

            if request.method == HttpMethod.GET:
                query_dict = request.GET
                multi_value_dict = QueryDict()
                form = ValidationForm(query_dict)

            elif request.method == HttpMethod.POST:
                query_dict = request.POST
                multi_value_dict = request.FILES
                form = ValidationForm(query_dict, multi_value_dict)

            else:
                query_dict, multi_value_dict = MultiPartParser(request.META, request, request.upload_handlers).parse()
                form = ValidationForm(query_dict)

            if not form.is_valid():
                return JSONResponse(error=form.errors, status=HttpStatus.BAD_REQUEST)

            mixed_kwargs = { **kwargs }

            if len(form.fields):
                mixed_kwargs['data'] = form.cleaned_data

            # TODO: Test file validation
            # if len(multi_value_dict):
            #     mixed_kwargs['files'] = multi_value_dict

            return func(request, *args, **mixed_kwargs)
        return wrapper
    return view_decorator