from swagger_client import RenameControllerApi
from swagger_client.api_client import ApiClient
from swagger_client.rest import ApiException

api_client = ApiClient()

rename_controller_api = RenameControllerApi(api_client)

old_file_name = "folder1/folder2/folder3/pisa.jpg"
new_file_name = "Italy.jpg"

try:
    response = rename_controller_api.rename_file(old_file_name, new_file_name)
    print(response)
except ApiException as e:
    print(e.body)
