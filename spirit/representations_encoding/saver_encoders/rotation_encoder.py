from spirit.saver_protobuf.saver_proto_pb2 import Field


def encode_rotation(rotation, _):
    rotation_field = Field()
    rotation_field.field_name = "rotation"
    rotation_field.field_value.value_type = "sub_fields"
    fields = ['x', 'y', 'z', 'w']
    for i in range(len(rotation)):
        sub_field = create_sub_fields(fields[i], rotation[i])
        rotation_field.field_value.sub_fields_value.append(sub_field)
    return rotation_field

def create_sub_fields(field_name, field_value):
    sub_field = Field()
    sub_field.field_name = field_name
    sub_field.field_value.value_type = "double"
    sub_field.field_value.double_value = field_value
    return sub_field


encode_rotation.field = "rotation"
