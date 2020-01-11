

def run_server(port, data_dir):
    """
    @address: address to run server in format (ip,port)
    @data_dir: the directory to save thoughts to
    run the server in address and save data inside a file in data_dir
    """
    from spirit.server import Server
    Server("localhost", port, data_dir).run_server()


def upload_snapshots(path, port):
    """
    upload snapshots in path to localhost:port
    """
    from spirit.client import Client
    Client(path, port).upload_snapshots()


def read(path):
    from .reader import reader
    rd = reader.Reader(path)
    for snapshot in rd:
        print(snapshot.depth_image)
