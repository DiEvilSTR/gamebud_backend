from django.contrib.auth import logout

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.validation.no_data_form import NoDataForm


@view(methods={ HttpMethod.GET: False, HttpMethod.POST: True }, RequestForm=NoDataForm)
def logout_view(request):
    logout(request)

    return JSONResponse(None)
