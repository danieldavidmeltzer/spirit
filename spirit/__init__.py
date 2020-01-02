from .reader import reader


def run_server(port, data_dir):
    """
    @address: address to run server in format (ip,port)
    @data_dir: the directory to save thoughts to
    run the server in address and save data inside a file in data_dir
    """
    import spirit.server as server
    server.run_server("localhost", port, data_dir)


def upload_snapshots(path, port):
    """
    upload snapshots in path
    """
    import spirit.client as client
    rd = reader.Reader(path)
    for snapshot in rd:
        client.upload_snapshot(snapshot, f"http://localhost:{port}")


def read(path):
    rd = reader.Reader(path)
    for snapshot in rd:
        print(snapshot.depth_image)
