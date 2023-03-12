# swagger_client.BrowseControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_folder**](BrowseControllerApi.md#browse_folder) | **GET** /remotestorage/browseFolder | 

# **browse_folder**
> str browse_folder(folder_path)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BrowseControllerApi()
folder_path = 'folder_path_example' # str | 

try:
    api_response = api_instance.browse_folder(folder_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrowseControllerApi->browse_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_path** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

