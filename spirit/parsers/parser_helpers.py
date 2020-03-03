import pika
import logging
from . import parser
from spirit.inner_protobuf.inner_protocol_pb2 import \
    SnapshotPacketInner
from spirit.representation_construction.protobuf_construction.protobuf_parsers \
    import inner_protobuf_parser
from .parsing_context import ParsingContext


def run_parser(parser_field, snapshot, blob_url=None):
    protobuf_snapshot_packet = SnapshotPacketInner()
    protobuf_snapshot_packet.ParseFromString(snapshot)
    snapshot_represented = \
        inner_protobuf_parser.parse_inner_protobuf(protobuf_snapshot_packet)
    parsing_context = ParsingContext.build_context(blob_url)
    return parser.parse_snapshot(snapshot_represented,
                                 parser_field,
                                 parsing_context)


def run_mq_parser(parser_field, mq_url, blob_url=None):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=mq_url))
    channel = connection.channel()

    channel.exchange_declare(exchange='parsing', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='parsing', queue=queue_name)

    logging.info('Waiting for snapshots.')

    def callback(ch, method, properties, body):
        parser_result = run_parser(parser_field, body, blob_url)
        publish_parser_result(parser_field, mq_url, parser_result)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()


def publish_parser_result(parser_field, mq_url, parser_result):
    pass
