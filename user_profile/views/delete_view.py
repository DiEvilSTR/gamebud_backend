from django.contrib.auth.models import User
from django.contrib.auth import logout

from utils.http.responses.JSONResponse import JSONResponse
from utils.http.constants import HttpMethod
from utils.http.decorators.views.view import view
from utils.validation.no_data_form import NoDataForm


@view(delete=NoDataForm)
def delete_view(request):
    user = User.objects.get(username=request.user.username)
    
    logout(request)
    user.delete()
    
    return JSONResponse(None)
