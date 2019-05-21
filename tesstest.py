import tessitura
import os

## test the connection to the tessitura API

endpoint = os.environ['TESSITURA_API']
credentials = os.environ['TESSITURA_CREDENTIALS']

method = "Diagnostics/Status"

request_type = "GET"

params = {}
data = {}

rsp = tessitura.rest_call(endpoint, credentials, request_type, method, params, data)

print(rsp)