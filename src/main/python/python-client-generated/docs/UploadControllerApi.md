# swagger_client.UploadControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file**](UploadControllerApi.md#upload_file) | **POST** /remotestorage/uploadFile | 

# **upload_file**
> str upload_file(body=body, path=path)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadControllerApi()
body = swagger_client.RemotestorageUploadFileBody() # RemotestorageUploadFileBody |  (optional)
path = '' # str |  (optional)

try:
    api_response = api_instance.upload_file(body=body, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadControllerApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemotestorageUploadFileBody**](RemotestorageUploadFileBody.md)|  | [optional] 
 **path** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

