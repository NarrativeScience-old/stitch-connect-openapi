# openapi_client.DestinationTypesApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_get_destination_types**](DestinationTypesApi.md#api_get_destination_types) | **GET** /v4/destination-types | Retrieves general information about the configuration required for all supported destination types. 


# **api_get_destination_types**
> list[DestinationReportCard] api_get_destination_types()

Retrieves general information about the configuration required for all supported destination types. 

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
api_instance = openapi_client.DestinationTypesApi(openapi_client.ApiClient(configuration))

try:
    # Retrieves general information about the configuration required for all supported destination types. 
    api_response = api_instance.api_get_destination_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DestinationTypesApi->api_get_destination_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DestinationReportCard]**](DestinationReportCard.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of destination report card objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

