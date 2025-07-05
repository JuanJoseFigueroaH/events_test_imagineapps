from azure.storage.blob import BlobServiceClient
import os
from uuid import uuid4

class AzureBlobService:
    def __init__(self):
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = os.getenv("AZURE_CONTAINER_NAME", "event-images")
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def upload_image(self, file_data: bytes, filename: str, content_type: str) -> str:
        unique_filename = f"{uuid4()}_{filename}"
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=unique_filename)
        blob_client.upload_blob(file_data, blob_type="BlockBlob", content_settings={"content_type": content_type})
        return blob_client.url
