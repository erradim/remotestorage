from swagger_client import UploadControllerApi, ApiClient

api_client = ApiClient()
api = UploadControllerApi(api_client)

file_name = 'pisa.jpg'

with open(file_name, 'rb') as f:
    content = f.read()

response = api.upload_file(path='')
print(response.data.decode())
