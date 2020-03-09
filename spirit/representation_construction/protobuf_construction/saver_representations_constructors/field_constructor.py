from spirit.representations_saver.represnetation_field_composite \
    import RepresentationFieldComposite
from spirit.representations_saver.represntation_field_simple \
    import RepresentationFieldSimple
from spirit.utils.exceptions import NoMatchingType


def construct_field(field_protobuf, parse_item):
    """
    construct result from result_protobuf
    Args:
        field_protobuf:
        result as described in:
        `
        message Field{
        message FieldValue{
        // value would be one of int, double, string, sub_fields
            string value_type = 1;
            int32 int_value = 2;
            string string_value = 3;
            double double_value = 4;
            repeated Field sub_fields_value = 5;
        }
        string field_name = 1;
        FieldValue field_value = 2;
        }
        `

        parse_item:
        for further parsing

    Returns:
        -RepresentationFieldSimple for field with int, double, string FieldValue
        -RepresentationFieldComposite for field with sub_fields FieldValue

    """
    if field_protobuf.field_value.value_type == "sub_fields":
        return construct_composite_result(field_protobuf, parse_item)
    else:
        return construct_simple_result(field_protobuf)


def construct_composite_result(result_protobuf, parse_item):
    sub_fields = list(map(parse_item,
                          result_protobuf.field_value.sub_fields_value))
    field_name = result_protobuf.field_name
    return RepresentationFieldComposite(field_name, sub_fields)


def construct_simple_result(result_protobuf):
    val_type = result_protobuf.field_value.value_type
    value = None
    if val_type == "int":
        value = result_protobuf.field_value.int_value
    elif val_type == "double":
        value = result_protobuf.field_value.double_value
    elif val_type == "string":
        value = result_protobuf.field_value.string_value
    else:
        raise NoMatchingType()
    return RepresentationFieldSimple(result_protobuf.field_name, value)


construct_field.field = "Field"
