from spirit.saver_protobuf.saver_proto_pb2 import Field


def encode_image_url(image_result, _, result):
    image_url = image_result[1]
    parser_name = image_result[0]
    result.parser_name = parser_name
    field = Field()
    field.field_name = "image_url"
    field.field_value.value_type = "string"
    field.field_value.string_value = image_url
    result.parser_fields.append(field)


encode_image_url.field = "ImageUrl"
