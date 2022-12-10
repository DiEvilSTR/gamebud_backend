from django.http import HttpResponse
import json

class JSONResponse(HttpResponse):
    def __init__(self, data=None, *args, error=None, **kwargs):
        normalized_data = {
            'data': None if error != None else data,
            'error': error,
        }
        
        serialized = json.dumps(normalized_data, default=str, separators=(',', ':'))

        super(JSONResponse, self).__init__(serialized, content_type='application/json', *args, **kwargs)