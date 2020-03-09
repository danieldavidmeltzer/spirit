import sys
import click
import logging
from purl import URL
from .parser_helpers import run_parser
from .parser_helpers import run_mq_parser


@click.group()
def main():
    pass


@main.command()
@click.argument('parser')
@click.argument('snapshot_path')
@click.option('-b', '--blob_url')
def parse(parser, snapshot_path, blob_url):
    with open(snapshot_path, "rb") as reader:
        snapshot = reader.read()
        parsing_result = run_parser(parser, snapshot, blob_url)
        print(parsing_result)


@main.command(name="run-parser")
@click.argument('parser')
@click.argument('mq_url')
@click.option('-b', '--blob_url')
def start_parser(parser, mq_url, blob_url):
    run_mq_parser(parser, mq_url, blob_url)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(process)d-%(levelname)s-%(message)s')
        main(prog_name="spirit.client/parsers")
    except Exception as error:
        logging.exception(f"Error: {error}, exiting")
        sys.exit(1)
