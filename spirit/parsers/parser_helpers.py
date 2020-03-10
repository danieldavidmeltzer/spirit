import logging

import pika
from purl import URL

from spirit.blob_store.secret_keys import get_minio_keys_from_environment
from spirit.inner_protobuf.inner_protocol_pb2 import \
    SnapshotPacketInner
from spirit.representation_construction.\
    protobuf_construction.protobuf_parsers \
    import inner_protobuf_parser
from spirit.representations_encoding.helper_encoders import saver_encoder
from . import parser
from .parsing_context import ParsingContext


def get_snapshot_packet_represented(snapshot_packet):
    protobuf_snapshot_packet = SnapshotPacketInner()
    protobuf_snapshot_packet.ParseFromString(snapshot_packet)
    snapshot_packet_represented = \
        inner_protobuf_parser.parse_inner_protobuf(protobuf_snapshot_packet)
    return snapshot_packet_represented


def run_parser(parser_field, snapshot_packet, blob_url=None):
    snapshot_packet_represented = \
        get_snapshot_packet_represented(snapshot_packet)
    snapshot_represented = snapshot_packet_represented.snapshot
    keys = None
    if blob_url:
        keys = get_minio_keys_from_environment()

    parsing_context = ParsingContext. \
        build_context(blob_url, keys)
    return parser.parse_snapshot(snapshot_represented,
                                 parser_field,
                                 parsing_context)


def run_mq_parser(parser_field, mq_url, blob_url=None):
    url = URL(mq_url)
    connection_parameters = pika.ConnectionParameters(host=url.host(),
                                                      port=url.port())
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='parsing', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='parsing', queue=queue_name)

    logging.info('Waiting for snapshots.')

    def callback(ch, method, properties, body):
        parser_result = run_parser(parser_field, body, blob_url)
        snapshot_packet_represented = get_snapshot_packet_represented(body)
        publish_parser_result(parser_field,
                              mq_url,
                              parser_result,
                              snapshot_packet_represented)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()


def publish_parser_result(parser_field,
                          mq_url,
                          parser_result,
                          snapshot_packet):
    user = snapshot_packet.user
    snapshot = snapshot_packet.snapshot
    parser_result = (parser_field, parser_result)
    result = (snapshot, user, parser_result)
    encoded_result = saver_encoder.encode_item(result, "ParsingResult")
    serialized_result = encoded_result.SerializeToString()
    url = URL(mq_url)
    connection_parameters = pika.ConnectionParameters(host=url.host(),
                                                      port=url.port())
    connection = pika.BlockingConnection(
        connection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue='saver', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='saver',
        body=serialized_result,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    connection.close()
