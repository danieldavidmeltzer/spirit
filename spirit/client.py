import logging
from concurrent.futures import ThreadPoolExecutor

import requests

from spirit.representations_encoding import encoder
from .reader import reader
from .utils.list_utils import lower_list


class Client:
    def __init__(self, path, port):
        self.path = path
        self.port = port

    def upload_snapshots(self):
        rd = reader.Reader(self.path)
        with ThreadPoolExecutor(10) as executor:
            for snapshot in rd:
                upload = executor.submit(upload_snapshot,
                                         snapshot,
                                         f"http://localhost:{self.port}")
                logging.info(upload.result())


def upload_snapshot(snapshot, server_url):
    available_fields = get_available_fields(server_url)
    snapshot_in_protobuf = encoder.encode_item(snapshot)
    remove_unneeded_fields(snapshot_in_protobuf, available_fields)
    r = requests.post(server_url + "/upload_snapshot",
                      data=snapshot_in_protobuf.SerializeToString())
    return r.text


def remove_unneeded_fields(snapshot, required_fields):
    """
    remove unsupported fields from protobuf item by setting them to None
    reduces size of item to send. could be crucial if image is not needed
    """
    required_fields_lowered = lower_list(required_fields)
    snapshot_var_keys = lower_list(snapshot.DESCRIPTOR.fields_by_name.keys())
    for var_key in snapshot_var_keys:
        if var_key not in required_fields_lowered:
            snapshot.ClearField(var_key)
            logging.debug(f"cleared {var_key} from snapshot at date:"
                          f"{snapshot.datetime}")


def get_available_fields(server_url):
    r = requests.get(server_url + "/get_parsers")
    return r.json()
