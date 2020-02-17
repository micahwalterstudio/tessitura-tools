__import__('pkg_resources').declare_namespace(__name__)

import requests

import json
import base64

def rest_call(endpoint, credentials, request_type, method, *args, **kwargs):

    params = kwargs.get('params', None)
    data = kwargs.get('data', None)
    timeout = kwargs.get('timeout', 15)

    url = endpoint + method

    # set up headers
   
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': api_prepare_auth_string(credentials)
    }

    # make the api call
    response = {}

    try:
        if request_type == "GET":
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
        elif request_type == "POST":
            response = requests.request("POST", url, data=str(data), headers=headers, timeout=timeout)
        elif request_type == "PUT":
            response = requests.request("PUT", url, data=str(data), headers=headers, timeout=timeout)
        elif request_type == "DELETE":
            response = requests.delete(url, headers=headers, timeout=timeout)
    
    # handle request errors
    except Exception as e:
        
        error = {
            "error": 500,
            "message": "Time Out Error connecting to Tessitura",
            "info": e
        }

        return error

    # handle errors from tessitura    
    if response.status_code != 200:
        rsp = {
            "error": response.status_code,
            "message": response.reason,
        }

        if response.text:
            rsp["info"] = response.json()

    # handle success
    else:
        if response.text:
            rsp = response.json()
        else:
            rsp = {}
    
    return rsp


def api_prepare_auth_string(credentials):

    encoded = base64.b64encode(str.encode(credentials))
    encoded = str(encoded.decode())
    authHeader = 'Basic ' + encoded

    return authHeader



