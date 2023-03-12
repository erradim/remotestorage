## Development Process (Java-first)

I started by coding the service business implementation in Java, and then leveraged tools provided by the chosen technology (Spring Boot with Springdoc-OpenAPI) to generate the service API. Lastly, I developped the Python consumer using the generated RemoteStorage OpenAPI definiton.

### Developing the Java provider
To develop the Java provider, the following steps were taken:
- Created a Gradle project, customized with the necessary Spring Boot dependencies.
- I used an initialized Gradle project my work directory for this project
- Wrote the RemoteStorage service business implementation:
- Controllers in the project:
  - BrowseController.java
  - DeleteController.java
  - DownloadController.java
  - RenameController.java
  - UploadController.java
- Marked it as a web service through the @RestController Spring annotation.

### Generate the OpenAPI Service Description
The OpenAPI service description was generated using the Springdoc-OpenAPI generation tool. The following steps were taken:
- Added 'org.springdoc:springdoc-openapi-ui:1.5.5' dependency to build.gradle
- Accessed `http://localhost:8080/v3/api-docs`
- Copied the output. This is our Calculator OpenAPI definition

### Develop the Python consumer
To develop the Python consumer, the following steps were taken:
- GenerateD a Python client stub from the generated RemoteStorage OpenAPI definition using [SwaggerHub.com](https://www.swaggerhub.com)
- Unzip the generated python code under `src/main/python/`
- Get to the unzipped folder and run: `python setup.py install`
- Wrote the consumer files under: `src/main/python/`
  - browse.py
  - delete.py
  - download.py
  - rename.py
  - upload.py
