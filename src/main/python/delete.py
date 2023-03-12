from swagger_client.api_client import ApiClient
from swagger_client import DeleteControllerApi
from swagger_client.rest import ApiException

api_client = ApiClient()
delete_api = DeleteControllerApi(api_client)

file_name = "folder1/folder2/folder3/pisa.jpg"

try:
    response = delete_api.delete_file(file_name)
    print(response)
except ApiException as e:
    print(e.body)
