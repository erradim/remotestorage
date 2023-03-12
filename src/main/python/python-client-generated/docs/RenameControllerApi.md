# swagger_client.RenameControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rename_file**](RenameControllerApi.md#rename_file) | **PUT** /remotestorage/renameFile | 

# **rename_file**
> str rename_file(old_file_name, new_file_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RenameControllerApi()
old_file_name = 'old_file_name_example' # str | 
new_file_name = 'new_file_name_example' # str | 

try:
    api_response = api_instance.rename_file(old_file_name, new_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RenameControllerApi->rename_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_file_name** | **str**|  | 
 **new_file_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

