from spirit.representation_construction.protobuf_construction import \
    saver_representations_constructors
from spirit.representation_construction.protobuf_construction.protobuf_parse \
    import parse_protobuf_item


def parse_saver_protobuf(protobuf_item, **kwargs):
    return parse_protobuf_item(protobuf_item,
                               saver_representations_constructors,
                               **kwargs)
