# swagger_client.DownloadControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file**](DownloadControllerApi.md#download_file) | **GET** /remotestorage/downloadFile | 

# **download_file**
> str download_file(file_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadControllerApi()
file_name = 'file_name_example' # str | 

try:
    api_response = api_instance.download_file(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadControllerApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

