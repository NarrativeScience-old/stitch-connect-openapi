# openapi_client.SourcesApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_get_sources**](SourcesApi.md#api_get_sources) | **GET** /v4/sources | Lists the sources for an account, including active, paused, and deleted sources. 


# **api_get_sources**
> list[Source] api_get_sources()

Lists the sources for an account, including active, paused, and deleted sources. 

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.stitchdata.com
configuration.host = "https://api.stitchdata.com"
# Create an instance of the API class
api_instance = openapi_client.SourcesApi(openapi_client.ApiClient(configuration))

try:
    # Lists the sources for an account, including active, paused, and deleted sources. 
    api_response = api_instance.api_get_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->api_get_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Source]**](Source.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of source objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

