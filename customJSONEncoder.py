import datetime
import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        return super().default(obj)