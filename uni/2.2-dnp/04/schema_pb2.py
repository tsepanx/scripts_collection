# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\"\x0e\n\x0c\x45mptyMessage\"=\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\r\x12\x16\n\tuser_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0c\n\n_user_name\"!\n\x0f\x42ooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\" \n\x08UserList\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User2{\n\x08\x44\x61tabase\x12\"\n\x07PutUser\x12\x05.User\x1a\x10.BooleanResponse\x12%\n\nDeleteUser\x12\x05.User\x1a\x10.BooleanResponse\x12$\n\x08GetUsers\x12\r.EmptyMessage\x1a\t.UserListb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYMESSAGE._serialized_start=16
  _EMPTYMESSAGE._serialized_end=30
  _USER._serialized_start=32
  _USER._serialized_end=93
  _BOOLEANRESPONSE._serialized_start=95
  _BOOLEANRESPONSE._serialized_end=128
  _USERLIST._serialized_start=130
  _USERLIST._serialized_end=162
  _DATABASE._serialized_start=164
  _DATABASE._serialized_end=287
# @@protoc_insertion_point(module_scope)