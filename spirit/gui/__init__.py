from .gui_server import GUIServer


def run_server(host, port, api_host, api_port):
    """
    run gui server
    Args:
        host: host of gui
        api_host: host of the api server
        api_port: port of the api server
        port: port of gui

    """
    GUIServer(host, port, api_host, api_port).run()
