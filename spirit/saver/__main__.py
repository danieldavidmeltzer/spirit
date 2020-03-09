import click
import pika
import sys
import logging
from purl import URL
from .saver import Saver


@click.group()
def main():
    pass


@main.command(name='run-saver')
@click.argument('database')
@click.argument('message_queue')
def run_saver(database, message_queue):
    """
    run saver to listen
    to
    <message_queue>
    and save
    to
    <database>
    """
    saver = Saver(database)
    url = URL(message_queue)
    connection_parameters = pika.ConnectionParameters(host=url.host(),
                                                      port=url.port())
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue='saver', durable=True)

    def callback(ch, method, properties, body):
        saver.save(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='saver', on_message_callback=callback)

    channel.start_consuming()


@main.command(name='save')
@click.argument('result')
@click.option('-d', '--database',
              default='mongodb://127.0.0.1:27017',
              show_default=True)
def save(result_path, database):
    """
    \b
    save data from
    <result>
    to
    <database>
    """
    with open(result_path,'rb') as reader:
        saver = Saver(database)
        saver.save(reader.read())


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO,
                            format='%(process)d-%(levelname)s-%(message)s')
        main(prog_name="spirit.saver/saver")
    except Exception as error:
        logging.exception(f"Error: {error}, exiting")
        sys.exit(1)
