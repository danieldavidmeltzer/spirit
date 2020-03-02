import sys
import click
import logging
from .server import Server


@click.group()
def main():
    pass


def run_server(host, port, publish):
    """
    run the server at <host>:<port>
    with method publish to publish the snapshots
    """
    Server(host, port, publish).run_server()


@main.command(name='run-server')
@click.argument('message_queue')
@click.argument('blob_store')
@click.option('-h', '--host', default='127.0.0.1', show_default=True)
@click.option('-p', '--port', type=int, default=8000, show_default=True)
def run_server_cli(message_queue, blob_store, host, port):
    """
    \b
    Run a server
    -- at --
    <host>:<port>
    listening to snapshots,
    pre-process and
    publish received snapshots
    -- to --
    <message_queue>.
    Using blob store
    -- at --
    <blob_store>
    """
    logging.debug(f"cli asked starting listening at {host}:{port} "
                  f"using MQ:{message_queue}")

    def publish_to_message_queue(message):
        print(message.snapshot.date_time)

    run_server(host, port, publish_to_message_queue)


if __name__ == '__main__':
    try:
        main(prog_name="spirit.server/server")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
