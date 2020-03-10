import os

from .keys import *


def get_minio_keys_from_environment():
    """

    Returns: dictionary with keys

    """
    return {MINIO_ACCESS_KEY: os.environ[ENV_MINIO_ACCESS_KEY],
            MINIO_SECRET_KEY: os.environ[ENV_MINIO_SECRET_KEY]}
