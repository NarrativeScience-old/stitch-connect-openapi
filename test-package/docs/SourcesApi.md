# openapi_client.SourcesApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_create_source**](SourcesApi.md#api_create_source) | **POST** /v4/sources | Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed. 
[**api_get_last_connection_check**](SourcesApi.md#api_get_last_connection_check) | **GET** /v4/sources/{source_id}/last-connection-check | Retrieves the last connection check for a source by the source’s unique identifier. 
[**api_get_sources**](SourcesApi.md#api_get_sources) | **GET** /v4/sources | Lists the sources for an account, including active, paused, and deleted sources. 
[**api_start_replication**](SourcesApi.md#api_start_replication) | **POST** /v4/sources/{source_id}/sync | Manually starts a replication job for a source using the source’s unique identifier. 


# **api_create_source**
> Source api_create_source(inline_object=inline_object)

Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed. 

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
inline_object = openapi_client.InlineObject() # InlineObject |  (optional)

try:
    # Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed. 
    api_response = api_instance.api_create_source(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->api_create_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created new source |  -  |
**400** | Cron expressions can’t specify both a day-of-week and day-of-month  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_last_connection_check**
> ConnectionCheck api_get_last_connection_check(source_id)

Retrieves the last connection check for a source by the source’s unique identifier. 

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
source_id = 'source_id_example' # str | The ID of the source

try:
    # Retrieves the last connection check for a source by the source’s unique identifier. 
    api_response = api_instance.api_get_last_connection_check(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->api_get_last_connection_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 

### Return type

[**ConnectionCheck**](ConnectionCheck.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved last connection check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **api_start_replication**
> ErrorObject api_start_replication(source_id)

Manually starts a replication job for a source using the source’s unique identifier. 

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
source_id = 'source_id_example' # str | The ID of the source

try:
    # Manually starts a replication job for a source using the source’s unique identifier. 
    api_response = api_instance.api_start_replication(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->api_start_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 

### Return type

[**ErrorObject**](ErrorObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Replication job already in progress |  -  |
**400** | Source has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

