# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: saver-proto.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='saver-proto.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11saver-proto.proto\"d\n\rParsingResult\x12 \n\x08snapshot\x18\x01 \x01(\x0b\x32\x0e.SnapshotSaver\x12\x18\n\x04user\x18\x02 \x01(\x0b\x32\n.UserSaver\x12\x17\n\x06result\x18\x03 \x01(\x0b\x32\x07.Result\"\x99\x02\n\x06Result\x12\x13\n\x0bparser_name\x18\x01 \x01(\t\x12$\n\rparser_fields\x18\x02 \x03(\x0b\x32\r.Result.Field\x1a\xd3\x01\n\x05\x46ield\x12\x11\n\tfieldName\x18\x01 \x01(\t\x12,\n\nfieldValue\x18\x02 \x01(\x0b\x32\x18.Result.Field.FieldValue\x1a\x88\x01\n\nFieldValue\x12\x12\n\nvalue_type\x18\x01 \x01(\t\x12\x11\n\tint_value\x18\x02 \x01(\x05\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\x12\x14\n\x0c\x64ouble_value\x18\x04 \x01(\x01\x12\'\n\x10sub_fields_value\x18\x05 \x03(\x0b\x32\r.Result.Field\"\x98\x01\n\tUserSaver\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08\x62irthday\x18\x03 \x01(\r\x12&\n\x06gender\x18\x04 \x01(\x0e\x32\x16.UserSaver.GenderSaver\".\n\x0bGenderSaver\x12\x08\n\x04MALE\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\t\n\x05OTHER\x10\x02\"6\n\rSnapshotSaver\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x02 \x01(\x04\x62\x06proto3'
)



_USERSAVER_GENDERSAVER = _descriptor.EnumDescriptor(
  name='GenderSaver',
  full_name='UserSaver.GenderSaver',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MALE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=514,
  serialized_end=560,
)
_sym_db.RegisterEnumDescriptor(_USERSAVER_GENDERSAVER)


_PARSINGRESULT = _descriptor.Descriptor(
  name='ParsingResult',
  full_name='ParsingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='ParsingResult.snapshot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='ParsingResult.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='ParsingResult.result', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=121,
)


_RESULT_FIELD_FIELDVALUE = _descriptor.Descriptor(
  name='FieldValue',
  full_name='Result.Field.FieldValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_type', full_name='Result.Field.FieldValue.value_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='Result.Field.FieldValue.int_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='Result.Field.FieldValue.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='Result.Field.FieldValue.double_value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_fields_value', full_name='Result.Field.FieldValue.sub_fields_value', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=405,
)

_RESULT_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='Result.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldName', full_name='Result.Field.fieldName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fieldValue', full_name='Result.Field.fieldValue', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_FIELD_FIELDVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=405,
)

_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parser_name', full_name='Result.parser_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parser_fields', full_name='Result.parser_fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_FIELD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=405,
)


_USERSAVER = _descriptor.Descriptor(
  name='UserSaver',
  full_name='UserSaver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='UserSaver.user_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='UserSaver.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='birthday', full_name='UserSaver.birthday', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='UserSaver.gender', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERSAVER_GENDERSAVER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=560,
)


_SNAPSHOTSAVER = _descriptor.Descriptor(
  name='SnapshotSaver',
  full_name='SnapshotSaver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='SnapshotSaver.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='SnapshotSaver.datetime', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=616,
)

_PARSINGRESULT.fields_by_name['snapshot'].message_type = _SNAPSHOTSAVER
_PARSINGRESULT.fields_by_name['user'].message_type = _USERSAVER
_PARSINGRESULT.fields_by_name['result'].message_type = _RESULT
_RESULT_FIELD_FIELDVALUE.fields_by_name['sub_fields_value'].message_type = _RESULT_FIELD
_RESULT_FIELD_FIELDVALUE.containing_type = _RESULT_FIELD
_RESULT_FIELD.fields_by_name['fieldValue'].message_type = _RESULT_FIELD_FIELDVALUE
_RESULT_FIELD.containing_type = _RESULT
_RESULT.fields_by_name['parser_fields'].message_type = _RESULT_FIELD
_USERSAVER.fields_by_name['gender'].enum_type = _USERSAVER_GENDERSAVER
_USERSAVER_GENDERSAVER.containing_type = _USERSAVER
DESCRIPTOR.message_types_by_name['ParsingResult'] = _PARSINGRESULT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['UserSaver'] = _USERSAVER
DESCRIPTOR.message_types_by_name['SnapshotSaver'] = _SNAPSHOTSAVER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParsingResult = _reflection.GeneratedProtocolMessageType('ParsingResult', (_message.Message,), {
  'DESCRIPTOR' : _PARSINGRESULT,
  '__module__' : 'saver_proto_pb2'
  # @@protoc_insertion_point(class_scope:ParsingResult)
  })
_sym_db.RegisterMessage(ParsingResult)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {

  'Field' : _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {

    'FieldValue' : _reflection.GeneratedProtocolMessageType('FieldValue', (_message.Message,), {
      'DESCRIPTOR' : _RESULT_FIELD_FIELDVALUE,
      '__module__' : 'saver_proto_pb2'
      # @@protoc_insertion_point(class_scope:Result.Field.FieldValue)
      })
    ,
    'DESCRIPTOR' : _RESULT_FIELD,
    '__module__' : 'saver_proto_pb2'
    # @@protoc_insertion_point(class_scope:Result.Field)
    })
  ,
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'saver_proto_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  })
_sym_db.RegisterMessage(Result)
_sym_db.RegisterMessage(Result.Field)
_sym_db.RegisterMessage(Result.Field.FieldValue)

UserSaver = _reflection.GeneratedProtocolMessageType('UserSaver', (_message.Message,), {
  'DESCRIPTOR' : _USERSAVER,
  '__module__' : 'saver_proto_pb2'
  # @@protoc_insertion_point(class_scope:UserSaver)
  })
_sym_db.RegisterMessage(UserSaver)

SnapshotSaver = _reflection.GeneratedProtocolMessageType('SnapshotSaver', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTSAVER,
  '__module__' : 'saver_proto_pb2'
  # @@protoc_insertion_point(class_scope:SnapshotSaver)
  })
_sym_db.RegisterMessage(SnapshotSaver)


# @@protoc_insertion_point(module_scope)
