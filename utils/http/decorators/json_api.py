from django.http import HttpResponse
import functools

from utils.http.formatters.to_json_response import to_json_response

def json_api(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        
        if isinstance(data, HttpResponse):
            return data
        
        return to_json_response(data)
    
    return wrapper