# openapi_client.DestinationsApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_create_destination**](DestinationsApi.md#api_create_destination) | **POST** /v4/destinations | Creates a new destination. Only a single destination is supported per Stitch client account. 
[**api_delete_destination**](DestinationsApi.md#api_delete_destination) | **DELETE** /v4/destinations/{destination_id} | Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection. 
[**api_get_destinations**](DestinationsApi.md#api_get_destinations) | **GET** /v4/destinations | Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account. 
[**api_update_destination**](DestinationsApi.md#api_update_destination) | **PUT** /v4/destinations/{destination_id} | Updates an existing destination. Modifications to the type attribute are not supported. 


# **api_create_destination**
> api_create_destination(destination_info=destination_info)

Creates a new destination. Only a single destination is supported per Stitch client account. 

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
api_instance = openapi_client.DestinationsApi(openapi_client.ApiClient(configuration))
destination_info = openapi_client.DestinationInfo() # DestinationInfo | Object containing type and properties of a destination (optional)

try:
    # Creates a new destination. Only a single destination is supported per Stitch client account. 
    api_instance.api_create_destination(destination_info=destination_info)
except ApiException as e:
    print("Exception when calling DestinationsApi->api_create_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_info** | [**DestinationInfo**](DestinationInfo.md)| Object containing type and properties of a destination | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Only a single destination per account is allowed  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_delete_destination**
> api_delete_destination(destination_id)

Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection. 

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
api_instance = openapi_client.DestinationsApi(openapi_client.ApiClient(configuration))
destination_id = 'destination_id_example' # str | The ID of the destination to be updated or deleted

try:
    # Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection. 
    api_instance.api_delete_destination(destination_id)
except ApiException as e:
    print("Exception when calling DestinationsApi->api_delete_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The ID of the destination to be updated or deleted | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination successfully deleted  |  -  |
**400** | Invalid destination ID  |  -  |
**502** | Destination ID contains illegal characters  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_destinations**
> list[Destination] api_get_destinations()

Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account. 

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
api_instance = openapi_client.DestinationsApi(openapi_client.ApiClient(configuration))

try:
    # Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account. 
    api_response = api_instance.api_get_destinations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DestinationsApi->api_get_destinations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Destination]**](Destination.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of destination objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_update_destination**
> api_update_destination(destination_id, destination_form_properties=destination_form_properties)

Updates an existing destination. Modifications to the type attribute are not supported. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.DestinationsApi()
destination_id = 'destination_id_example' # str | The ID of the destination to be updated or deleted
destination_form_properties = openapi_client.DestinationFormProperties() # DestinationFormProperties | Object containing properties info (optional)

try:
    # Updates an existing destination. Modifications to the type attribute are not supported. 
    api_instance.api_update_destination(destination_id, destination_form_properties=destination_form_properties)
except ApiException as e:
    print("Exception when calling DestinationsApi->api_update_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The ID of the destination to be updated or deleted | 
 **destination_form_properties** | [**DestinationFormProperties**](DestinationFormProperties.md)| Object containing properties info | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid destination ID  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

