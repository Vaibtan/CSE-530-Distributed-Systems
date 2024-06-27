# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kmeans.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ckmeans.proto\x12\x06kmeans\"\x80\x01\n\rMapperRequest\x12\x11\n\tmapper_id\x18\x01 \x01(\x05\x12#\n\tcentroids\x18\x02 \x03(\x0b\x32\x10.kmeans.Centroid\x12\x13\n\x0brange_start\x18\x03 \x01(\x05\x12\x11\n\trange_end\x18\x04 \x01(\x05\x12\x0f\n\x07num_red\x18\x05 \x01(\x05\"3\n\x0eMapperResponse\x12\x11\n\tmapper_id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\"9\n\x0eReducerRequest\x12\x12\n\nreducer_id\x18\x01 \x01(\x05\x12\x13\n\x0bnum_mappers\x18\x02 \x01(\x05\"^\n\x0fReducerResponse\x12\x12\n\nreducer_id\x18\x01 \x01(\x05\x12\'\n\rnew_centroids\x18\x02 \x03(\x0b\x32\x10.kmeans.Centroid\x12\x0e\n\x06status\x18\x03 \x01(\t\">\n\x13IntermediateRequest\x12\x12\n\nreducer_id\x18\x01 \x01(\x05\x12\x13\n\x0bnum_mappers\x18\x02 \x01(\x05\"8\n\x14IntermediateResponse\x12\x12\n\nreducer_id\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\t\"\"\n\x0f\x41\x63knowledgement\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x08\x43\x65ntroid\x12\x13\n\x0b\x63oordinates\x18\x01 \x03(\x01\x32\xcb\x02\n\rKMeansCluster\x12\x41\n\x10SendDataToMapper\x12\x15.kmeans.MapperRequest\x1a\x16.kmeans.MapperResponse\x12K\n\x17ReceiveUpdatedCentroids\x12\x17.kmeans.ReducerResponse\x1a\x17.kmeans.Acknowledgement\x12H\n\x15ProcessDataForReducer\x12\x16.kmeans.ReducerRequest\x1a\x17.kmeans.ReducerResponse\x12`\n#send_intermediate_values_to_reducer\x12\x1b.kmeans.IntermediateRequest\x1a\x1c.kmeans.IntermediateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kmeans_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MAPPERREQUEST']._serialized_start=25
  _globals['_MAPPERREQUEST']._serialized_end=153
  _globals['_MAPPERRESPONSE']._serialized_start=155
  _globals['_MAPPERRESPONSE']._serialized_end=206
  _globals['_REDUCERREQUEST']._serialized_start=208
  _globals['_REDUCERREQUEST']._serialized_end=265
  _globals['_REDUCERRESPONSE']._serialized_start=267
  _globals['_REDUCERRESPONSE']._serialized_end=361
  _globals['_INTERMEDIATEREQUEST']._serialized_start=363
  _globals['_INTERMEDIATEREQUEST']._serialized_end=425
  _globals['_INTERMEDIATERESPONSE']._serialized_start=427
  _globals['_INTERMEDIATERESPONSE']._serialized_end=483
  _globals['_ACKNOWLEDGEMENT']._serialized_start=485
  _globals['_ACKNOWLEDGEMENT']._serialized_end=519
  _globals['_CENTROID']._serialized_start=521
  _globals['_CENTROID']._serialized_end=552
  _globals['_KMEANSCLUSTER']._serialized_start=555
  _globals['_KMEANSCLUSTER']._serialized_end=886
# @@protoc_insertion_point(module_scope)
