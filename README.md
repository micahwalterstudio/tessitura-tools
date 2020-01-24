# Tessitura

Tools for talking to the Tessitura API from Python. This is all just wet paint at the moment.

Requires Python 3.6+

To install just do:

```
$ pip install tessitura
```

To use see the following example:

```
import tessitura
import pprint

endpoint = "https://your.tessitura-endpoint.org/TessituraService/"
credentials = "username:group:location:password"

# The REST API method you wish to call. This may need to be created with other information depending on the request, such as a session id -- See Tessitura documentation for more information. Please note there should be no trailing slash at the end.

method = "Diagnostics/Status"

# The type of request you wish to make. Currently supports GET and POST.

request_type = "GET"

# Use this to add any query string parameters to a GET request
params = {}

# Use this to add any form data to a POST request
data = {}

# Call the API
rsp = tessitura.rest_call(endpoint, credentials, request_type, method, params=params, data=data, timeout=10)

# Print out the results in JSON format
pprint.pprint(rsp)