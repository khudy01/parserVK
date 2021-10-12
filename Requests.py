import requests
import json

def Request(request : str) -> bytes:
    response = requests.get(request)
    return json.loads(response.content)