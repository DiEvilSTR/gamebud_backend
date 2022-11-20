from django.http import HttpResponse
import json

class JSONResponse(HttpResponse):
    def __init__(self, data='', *args, **kwargs):
        serialized = json.dumps(data, default=str, separators=(',', ':'))

        super(JSONResponse, self).__init__(serialized, content_type='application/json', *args, **kwargs)