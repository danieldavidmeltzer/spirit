import sys
import click
from .parser_helpers import run_parser


@click.group()
def main():
    pass


@main.command()
@click.argument('parser')
@click.argument('snapshot_path')
@click.option('-h', '--blob_url')
def parse(parser, snapshot_path, blob_url):
    with open(snapshot_path, "rb") as reader:
        snapshot = reader.read()
        parsing_result = run_parser(parser, snapshot, blob_url)
        print(parsing_result)


@main.command(name="run-parser")
@click.argument('parser')
@click.argument('mq_url')
@click.option('-h', '--blob_url')
def start_parser(parser, mq_url, blob_url):
    pass


if __name__ == '__main__':
    try:
        main(prog_name="spirit.client/parsers")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
