import click

import spirit


@click.group()
def main():
    pass


@main.group()
def client():
    pass


@main.group()
def server():
    pass


@server.command(name='run')
@click.argument('dir_path')
@click.argument('port', type=click.INT)
def run_server(dir_path, port):
    """
    run server in dir_path at port
    """
    spirit.run_server(port, dir_path)


@client.command(name='run')
@click.argument('sample_path')
@click.argument('port', type=click.INT)
def run_client(sample_path, port):
    """
    run the client with path of sample_path in port
    """
    spirit.upload_snapshots(sample_path, port)


@main.command()
@click.argument('path')
def read(path):
    spirit.read(path)


if __name__ == '__main__':
    # try:
    main(prog_name="spirit")
    # except Exception as error:
    #     print(f"Error: {error}")
    #     sys.exit(1)
