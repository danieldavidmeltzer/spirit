import io
from purl import URL
from ..keys import *
from minio import Minio
from uuid import uuid4


class CustomBlobDriver:
    def __init__(self, url, keys):
        url = URL(url)
        minio_url = f"{url.host()}:{url.port()}"
        minio_access_key = keys[MINIO_ACCESS_KEY]
        minio_secret_key = keys[MINIO_SECRET_KEY]
        self.minio_client = Minio(minio_url,
                                  access_key=minio_access_key,
                                  secret_key=minio_secret_key,
                                  secure=False)

    def save_binary(self, binary):
        """
        save a binary to minio server, gives a unique uuid
        Args:
            binary:
                binary to save
        Returns:
            unique uuid given
        """
        binary_id = str(uuid4())  # random enough for no collisions
        io_stream = io.BytesIO(binary)
        self.minio_client.put_object(BUCKET_NAME_KEY,
                                     binary_id,
                                     io_stream,
                                     len(binary))
        return binary_id

    def get_binary(self, binary_id):
        """
        get a binary from minio server
        Args:
            binary_id: id of binary

        Returns:
            bytes object of saved binary data
        """
        response = self.minio_client.get_object(BUCKET_NAME_KEY, binary_id)
        return response.data


CustomBlobDriver.scheme = "custom.blob.scheme"
