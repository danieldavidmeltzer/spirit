import logging
import shutil
import sys
from io import BytesIO

import click
import requests
from PIL import Image

from .ascii_art import print_ascii_art


@click.group()
def main():
    pass


def get_address(host, port):
    return f"http://{host}:{port}"


@main.command(name='get-users')
@click.option('-h', '--host', default='localhost', show_default=True)
@click.option('-p', '--port', type=int, default=5000, show_default=True)
def get_users(host, port):
    """
    Returns:
    all users
    """
    addr = get_address(host, port) + "/users"
    response = requests.get(addr)
    result = response.json()
    for user_id in result:
        print(f"user {user_id} named {result[user_id]['name']}")


@main.command(name='get-user')
@click.argument("user_id")
@click.option('-h', '--host', default='localhost', show_default=True)
@click.option('-p', '--port', type=int, default=5000, show_default=True)
def get_user(user_id, host, port):
    addr = get_address(host, port) + f"/users/{user_id}"
    response = requests.get(addr)
    result = response.json()
    for item in result:
        print(f"user {item} {result[item]}")


@main.command(name='get-snapshots')
@click.argument("user_id")
@click.option('-h', '--host', default='localhost', show_default=True)
@click.option('-p', '--port', type=int, default=5000, show_default=True)
def get_snapshots(user_id, host, port):
    addr = get_address(host, port) + f"/users/{user_id}/snapshots"
    response = requests.get(addr)
    result = response.json()
    for snapshot in result:
        snapshot_obj = result[snapshot]

        print(f"snapshot {snapshot} from "
              f"{snapshot_obj['date_time']}")


@main.command(name='get-snapshot')
@click.argument("user_id")
@click.argument("snapshot_id")
@click.option('-h', '--host', default='localhost', show_default=True)
@click.option('-p', '--port', type=int, default=5000, show_default=True)
def get_snapshot(snapshot_id, user_id, host, port):
    addr = get_address(host, port)\
           + f"/users/{user_id}/snapshots/{snapshot_id}"
    response = requests.get(addr)
    result = response.json()
    results = result['results']
    snapshot_date = result['snapshot_date']
    print(f"snapshot {snapshot_id} from {snapshot_date}")
    print("results are:")
    for result in results:
        print(result)


@main.command(name='get-result')
@click.argument("user_id")
@click.argument("snapshot_id")
@click.argument("result")
@click.option('-h', '--host', default='localhost', show_default=True)
@click.option('-p', '--port', type=int, default=5000, show_default=True)
@click.option('-s', '--save', default=None)
@click.option('--art', is_flag=True)
def get_result(snapshot_id, user_id, result, host, port, save, art):
    addr = get_address(host, port) + f"/users/{user_id}/snapshots/" \
                                     f"{snapshot_id}/{result}"
    response = requests.get(addr)
    json_result = response.json()
    handle_result = None
    image_data = None
    if result == "pose":
        handle_pose(json_result)
    elif result == "feelings":
        handle_feelings(json_result)
    elif result in ["color_image", "depth_image"]:
        image_data = handle_image(addr, json_result, art, image_data)
    else:
        print(json_result)
        handle_result = str(json_result)

    if save:
        handle_save(addr, handle_result, image_data, result, save)


def handle_image(addr, json_result, art, image_data):
    print(f"image url:{json_result['image_url']}")
    if art:
        response = requests.get(addr + '/data')
        image_data = BytesIO(response.content)
        print_ascii_art(image_data)
    return image_data


def handle_save(addr, handle_result, image_data, result, save):
    if result in ["color_image", "depth_image"]:
        if image_data:
            image_data.seek(0)
            image = Image.open(image_data)
            image.save(save)
        else:
            response = requests.get(addr + '/data', stream=True)
            with open(save, 'wb') as out_file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, out_file)
    else:
        with open(save, "w") as saver:
            saver.write(handle_result)


def handle_feelings(json_result):
    print_result = "feelings:"
    for feeling in json_result:
        print_result += f"{feeling}:{json_result[feeling]}\n"
    print(print_result.rstrip())
    return print_result.rstrip()


def handle_pose(json_result):
    print_result = ""
    print_result += "pose:\n"
    print_result += "translation:\n"
    for v in json_result['translation']:
        print_result += f"{v}:{json_result['translation'][v]}\n"
    print_result += "rotation\n"
    for v in json_result['rotation']:
        print_result += f"{v}:{json_result['rotation'][v]}\n"
    print(print_result.rstrip())
    return print_result.rstrip()


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(process)d-%(levelname)s-%(message)s')
        main(prog_name="spirit.client/client")
    except Exception as error:
        logging.exception(f"Error: {error}, exiting")
        sys.exit(1)
