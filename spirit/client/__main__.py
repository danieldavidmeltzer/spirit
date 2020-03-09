import sys
import click
import logging
from .client import Client
import requests


@click.group()
def main():
    pass


@main.command(name='upload-sample')
@click.argument('file_path')
@click.option('-h', '--host', default='localhost', show_default=True)
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
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(process)d-%(levelname)s-%(message)s')
        main(prog_name="spirit.client/client")
    except requests.exceptions.RequestException as connection_error:
        print(f"can't connect: {connection_error}")
        logging.exception(f"connection error:{connection_error}, exiting")
        sys.exit(1)
    except Exception as error:
        logging.exception(f"Error: {error}, exiting")
        sys.exit(1)
