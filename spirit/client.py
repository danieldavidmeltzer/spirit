import requests
import jsonpickle


def upload_snapshot(snapshot, url):
    available_fields = get_available_fields(url)
    remove_unneeded_fields(snapshot, available_fields)
    requests.post(url+"/upload_snapshot",
                  json=jsonpickle.encode(snapshot))


def remove_unneeded_fields(snapshot, required_fields):
    snapshot_var_keys = [key for key in vars(snapshot)]
    for var_key in snapshot_var_keys:
        if var_key not in required_fields:
            delattr(snapshot, var_key)


def get_available_fields(server_url):
    r = requests.get(server_url+"/get_parsers")
    return r.json()

