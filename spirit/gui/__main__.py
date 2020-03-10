import logging
import sys

import click

from .gui_server import GUIServer


@click.group()
def main():
    pass


@main.command(name='run-server')
@click.option('-h', '--host', default='0.0.0.0', show_default=True)
@click.option('-p', '--port', default=8080, show_default=True)
@click.option('-H', '--api_host',
              default='127.0.0.1',
              show_default=True)
@click.option('-P', '--api_port',
              default=5000,
              show_default=True)
@click.option("-I", "image_api_address", default="127.0.0.1:5000")
def run_server(host, port, api_host, api_port, image_api_address):
    """
    run gui server
    Args:
        host: host of gui
        api_host: host of the api server
        api_port: port of the api server
        port: port of gui
        image_api_address: html way to fetch images

    """
    GUIServer(host, port, api_host, api_port, image_api_address).run()


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(process)d-%(levelname)s-%(message)s')
        main(prog_name="spirit.api/api")
    except Exception as error:
        logging.exception(f"Error: {error}, exiting")
        sys.exit(1)
