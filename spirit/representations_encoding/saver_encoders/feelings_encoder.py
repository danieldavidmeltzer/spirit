from spirit.saver_protobuf.saver_proto_pb2 import Field


def encode_feelings(feelings_result, _, result):
    feelings = feelings_result[1]
    parser_name = feelings_result[0]  # this should be 'feelings'
    result.parser_name = parser_name
    # could iterate all variables, but more explicit and I think, safe

    for feeling in ["hunger", "thirst", "exhaustion", "happiness"]:
        field = create_field_for_feeling(feeling, getattr(feelings, feeling))
        result.parser_fields.append(field)


def create_field_for_feeling(feeling_name, value):
    field = Field()
    field.field_name = feeling_name
    field.field_value.value_type = "double"
    field.field_value.double_value = value
    return field


encode_feelings.field = "feelings"
