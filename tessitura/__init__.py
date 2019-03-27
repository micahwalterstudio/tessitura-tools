__import__('pkg_resources').declare_namespace(__name__)

import requests

import json
import base64

def rest_call(endpoint, credentials, request_type, method, *args, **kwargs):

    params = kwargs.get('params', None)
    data = kwargs.get('data', None)

    url = endpoint + method

    r = {}
   
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': api_prepare_auth_string(credentials)
    }

    try:
        if request_type == "GET":
            r = requests.get(url, params=params, headers=headers, timeout=15)
        elif request_type == "POST":
            r = requests.request("POST", url, data=str(data), headers=headers, timeout=15)
    
    except Exception as e:
        
        timeout = {
            "error": 500,
            "message": "Time Out Error connecting to Tessitura",
            "e": e
        }

        return timeout
    
    if r.status_code != 200:
        
        j = {
            "error": r.status_code,
            "message": r.reason
        }     
    else:
        j = r.json()
    
    return j


def api_prepare_auth_string(credentials):

    encoded = base64.b64encode(str.encode(credentials))
    encoded = str(encoded.decode())
    authHeader = 'Basic ' + encoded

    return authHeader



