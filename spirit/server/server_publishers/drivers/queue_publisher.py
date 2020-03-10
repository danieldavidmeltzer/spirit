import pika
from purl import URL


def create_publisher(queue_url):
    def publisher(message):
        url = URL(queue_url)
        connection_params = pika.ConnectionParameters(host=url.host(),
                                                      port=url.port())
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        channel.exchange_declare(exchange='parsing', exchange_type='fanout')
        channel.basic_publish(exchange='parsing', routing_key='', body=message)
        connection.close()

    return publisher


create_publisher.scheme = "rabbitmq"
