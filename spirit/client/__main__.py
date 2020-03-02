import sys
import click
import logging
from .client import Client


@click.group()
def main():
    pass


@main.command(name='upload-sample')
@click.argument('file_path')
@click.option('-h', '--host', default='127.0.0.1', show_default=True)
@click.option('-p', '--port', type=int, default=8000, show_default=True)
def upload_sample(file_path, host, port):
    """
    \b
    Upload a sample
    -- from --
    <file_path>
    -- to --
    server at - <host>:<port>
    waiting to handle it.

    """
    logging.debug(f"client upload sample from:{file_path} to {host}:{port}")
    client = Client(file_path, host, port)
    client.upload_snapshots()


if __name__ == '__main__':
    main(prog_name="spirit.client/client")
    try:
        main(prog_name="spirit.client/client")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
