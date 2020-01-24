import tessitura
import os
import pprint

## test the connection to the tessitura API

endpoint = os.environ['TESSITURA_API']
credentials = os.environ['TESSITURA_CREDENTIALS']

method = "Web/Session" 
request_type = "POST"

data = {
    "IpAddress": "",
    "BusinessUnitId": 1,
    "Organization": ""
}

params = {}

rsp = tessitura.rest_call(endpoint, credentials, request_type, method, params=params, data=data, timeout=5)

pprint.pprint(rsp, indent=4)