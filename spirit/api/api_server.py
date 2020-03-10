from flask import Flask
from flask import jsonify
from flask import make_response

from spirit.blob_store.blob_store import BlobStore
from spirit.blob_store.secret_keys import get_minio_keys_from_environment
from spirit.utils.fetcher import find_driver
from . import database_drivers

app = Flask(__name__)


class APIServer:
    def __init__(self, host, port, database_url, blob_store):
        self.host = host
        self.port = port
        self.database_driver = find_driver(database_url, database_drivers)
        self.blob_store = blob_store

    def run(self):
        keys = get_minio_keys_from_environment()
        blob_client = BlobStore(self.blob_store, keys)
        app.config['database_driver'] = self.database_driver
        app.config['blob_client'] = blob_client
        app.run(host=self.host, port=self.port)


@app.route("/users")
def get_users():
    db_driver = app.config['database_driver']
    return jsonify(db_driver.get_users())


@app.route("/users/<int:user_id>")
def get_user(user_id):
    db_driver = app.config['database_driver']
    return jsonify(db_driver.get_user(user_id))


@app.route("/users/<int:user_id>/snapshots")
def get_snapshots(user_id):
    db_driver = app.config['database_driver']
    return jsonify(db_driver.get_snapshots(user_id))


@app.route('/users/<int:user_id>/snapshots/<snapshot_id>')
def get_snapshot(user_id, snapshot_id):
    db_driver = app.config['database_driver']
    return jsonify(db_driver.get_snapshot(snapshot_id))


@app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>')
def get_result(user_id, snapshot_id, result_name):
    db_driver = app.config['database_driver']
    return jsonify(db_driver.get_result(snapshot_id, result_name))


@app.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>/data')
def get_data(user_id, snapshot_id, result_name):
    db_driver = app.config['database_driver']
    blob_client = app.config['blob_client']
    if result_name.lower() in ['color_image', 'depth_image']:
        image_id = db_driver.get_image_id(snapshot_id, result_name)
        image = blob_client.get_binary(image_id)
        response = make_response(image)
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set(
            'Content-Disposition', 'attachment', filename='data.jpg')
        return response
    else:
        return {'error': f"Not supported 'data' field for result:{result_name}"}
