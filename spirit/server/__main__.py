import sys
import click
import logging
from .server import Server
from .server_publishers import server_publish


@click.group()
def main():
    pass


def run_server(host, port, blob_store, publish):
    """
    run the server at <host>:<port>
    with method publish to publish the snapshots
    """
    Server(host, port, blob_store,publish).run_server()


@main.command(name='run-server')
@click.argument('message_queue')
@click.argument('blob_store')
@click.option('-h', '--host', default='127.0.0.1', show_default=True)
@click.option('-p', '--port', type=int, default=8000, show_default=True)
def run_server_cli(publisher_url, blob_store, host, port):
    """
    \b
    Run a server
    -- at --
    <host>:<port>
    listening to snapshots,
    pre-process and
    publish received snapshots
    -- to --
    <publisher_url>.
    Using blob store
    -- at --
    <blob_store>
    """

    publisher = server_publish.find_publisher_driver(publisher_url)
    run_server(host, port, blob_store, publisher)


if __name__ == '__main__':
    try:
        main(prog_name="spirit.server/server")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
