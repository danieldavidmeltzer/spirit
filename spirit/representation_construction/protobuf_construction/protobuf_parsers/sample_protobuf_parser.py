from spirit.representation_construction.protobuf_construction import \
    sample_representations_constructors
from spirit.representation_construction.protobuf_construction.protobuf_parse import \
    parse_protobuf_item


def parse_sample_protobuf(protobuf_item, **kwargs):
    return parse_protobuf_item(protobuf_item,
                               sample_representations_constructors,
                               **kwargs)