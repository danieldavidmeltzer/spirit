import click
import sys
from .api_server import APIServer
import logging


@click.group()
def main():
    pass


@main.command(name='run-server')
@click.option('-h', '--host', default='0.0.0.0', show_default=True)
@click.option('-p', '--port', default=5000, show_default=True)
@click.option('-d', '--database',
              default='mongodb://127.0.0.1:27017',
              show_default=True)
@click.option('-b', '--blob_store',
              default='custom.blob.scheme://127.0.0.1:9000',
              show_default=True)
def run_api(database, host, port, blob_store):
    """
    run api server
    Args:
        database: data base to connect
        host: host of the api server
        port: port of the api server
        blob_store: the url of the blob store

    """
    APIServer(host, port, database, blob_store).run()


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(process)d-%(levelname)s-%(message)s')
        main(prog_name="spirit.api/api")
    except Exception as error:
        logging.exception(f"Error: {error}, exiting")
        sys.exit(1)
