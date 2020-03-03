import pika
from purl import URL


def create_publisher(queue_url):
    def publisher(message):
        url = URL(queue_url)
        host = f"{url.host()}:{url.port()}"
        connection_params = pika.ConnectionParameters(host)
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        channel.exchange_declare(exchange='parsing', exchange_type='fanout')
        channel.basic_publish(exchange='parsing', routing_key='', body=message)

    return publisher


create_publisher.scheme = "rabbitmq"
