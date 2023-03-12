from swagger_client import DownloadControllerApi, ApiClient

api_client = ApiClient()
api = DownloadControllerApi(api_client)

file_name = 'pisa.jpg'

content = api.download_file(file_name)

content = content.encode('utf-8')

with open(file_name, 'wb') as f:
    f.write(content)
