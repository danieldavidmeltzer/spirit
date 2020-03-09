from spirit.saver_protobuf.saver_proto_pb2 import Field


def encode_translation(translation, _):
    translation_field = Field()
    translation_field.field_name = "translation"
    translation_field.field_value.value_type = "sub_fields"
    fields = ['x', 'y', 'z']
    for i in range(len(translation)):
        sub_field = create_sub_fields(fields[i], translation[i])
        translation_field.field_value.sub_fields_value.append(sub_field)
    return translation_field


encode_translation.field = "translation"


def create_sub_fields(field_name, field_value):
    sub_field = Field()
    sub_field.field_name = field_name
    sub_field.field_value.value_type = "double"
    sub_field.field_value.double_value = field_value
    return sub_field
