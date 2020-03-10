import requests
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="../../website/",
            static_folder="../../website/")


class GUIServer:
    def __init__(self, host, port, api_host, api_port):
        self.host = host
        self.port = port
        app.config['api_host'] = api_host
        app.config['api_port'] = api_port

    def run(self):
        app.run(host=self.host, port=self.port)


def get_address(host, port):
    return f"http://{host}:{port}"


@app.route("/users")
def get_users():
    host = app.config['api_host']
    port = app.config['api_port']
    addr = get_address(host, port) + "/users"
    response = requests.get(addr)
    result = response.json()
    users = []
    for user_id in result:
        user = get_user_data(host, port, user_id)
        users.append(user)
    return render_template('index.html', users=users)


def get_user_data(host, port, user_id):
    addr = get_address(host, port) + f"/users/{user_id}"
    response = requests.get(addr)
    user = response.json()
    return user


@app.route("/users/<int:user_id>")
def get_user(user_id):
    host = app.config['api_host']
    port = app.config['api_port']
    addr = get_address(host, port) + f"/users/{user_id}/snapshots"
    response = requests.get(addr)
    snapshots = response.json()
    snapshots_final = []
    for snapshot in snapshots:
        snap = {'snapshot_id': snapshot,
                'date_time': snapshots[snapshot]['date_time']}
        snapshots_final.append(snap)
    host = '127.0.0.1' if host == "host.docker.internal" else host
    return render_template('user_page.html',
                           snapshot_f=snapshots_final[:1][0],
                           snapshots=snapshots_final[1:],
                           user_id=user_id,
                           host=host,
                           port=port)


@app.route('/users/<int:user_id>/snapshots/<snapshot_id>')
def get_snapshot(user_id, snapshot_id):
    host = app.config['api_host']
    port = app.config['api_port']
    addr_pose = get_address(host, port) + f"/users/{user_id}/snapshots/" \
                                          f"{snapshot_id}/pose"
    response_pose = requests.get(addr_pose)
    pose_result = response_pose.json()
    addr_feelings = get_address(host, port) + f"/users/{user_id}/snapshots/" \
                                              f"{snapshot_id}/feelings"
    response_feelings = requests.get(addr_feelings)
    feelings_result = response_feelings.json()
    for feeling in feelings_result:
        feelings_result[feeling] = int(90 * feelings_result[feeling])
    host = '127.0.0.1' if host == "host.docker.internal" else host
    return render_template('snapshot_data.html',
                           feelings=feelings_result,
                           translation=pose_result['translation'],
                           rotation=pose_result['rotation'],
                           snapshot_id=snapshot_id,
                           user_id=user_id,
                           host=host,
                           port=port)
