# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: text_storage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12text_storage.proto\x12\x0btextstorage\x1a\x1bgoogle/protobuf/empty.proto\"\x1b\n\x0bTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"&\n\x11TimestampResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"\x07\n\x05\x45mpty2\xe4\x01\n\x12TextStorageService\x12=\n\tStoreText\x12\x18.textstorage.TextRequest\x1a\x16.google.protobuf.Empty\x12H\n\x0cGetTimestamp\x12\x18.textstorage.TextRequest\x1a\x1e.textstorage.TimestampResponse\x12\x45\n\tQueryText\x12\x18.textstorage.TextRequest\x1a\x1e.textstorage.TimestampResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'text_storage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEXTREQUEST']._serialized_start=64
  _globals['_TEXTREQUEST']._serialized_end=91
  _globals['_TIMESTAMPRESPONSE']._serialized_start=93
  _globals['_TIMESTAMPRESPONSE']._serialized_end=131
  _globals['_EMPTY']._serialized_start=133
  _globals['_EMPTY']._serialized_end=140
  _globals['_TEXTSTORAGESERVICE']._serialized_start=143
  _globals['_TEXTSTORAGESERVICE']._serialized_end=371
# @@protoc_insertion_point(module_scope)