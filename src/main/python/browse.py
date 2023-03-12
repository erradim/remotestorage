from swagger_client import BrowseControllerApi, ApiClient
from swagger_client.rest import ApiException

api_client = ApiClient()

browse_api = BrowseControllerApi(api_client)

folder_path = "folder1/folder2/folder3"

try:
    folder_contents = browse_api.browse_folder(folder_path)
    print(folder_contents)
except ApiException as e:
    print(e.body)
