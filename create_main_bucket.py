import minio
import sys
import os

minio_client = minio.Minio(sys.argv[1],
                           access_key=os.environ["MINIO_ACCESS_KEY"],
                           secret_key=os.environ["MINIO_SECRET_KEY"],
                           secure=False)
minio_client.make_bucket("main-blob-bucket")
