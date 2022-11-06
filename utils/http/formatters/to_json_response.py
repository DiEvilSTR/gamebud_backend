from django.http import HttpResponse
import json

def to_json_response(data, **kwargs):
    serialized = json.dumps(data, default=str, separators=(',', ':'))
    
    return HttpResponse(serialized, content_type='application/json', **kwargs)