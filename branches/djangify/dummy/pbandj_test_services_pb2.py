# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import pbandj_test_pb2
import django_types_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='pbandj_test_services.proto',
  package='',
  serialized_pb='\n\x1apbandj_test_services.proto\x1a\x11pbandj_test.proto\x1a\x12\x64jango_types.proto2N\n\rSimpleService\x12\x1d\n\tgetSimple\x12\x07.Simple\x1a\x07.Simple\x12\x1e\n\ngetSimpler\x12\x07.Simple\x1a\x07.Simple2/\n\x0eSimplerService\x12\x1d\n\tsimplyGet\x12\x07.Simple\x1a\x07.SimpleB\x06\x88\x01\x01\x90\x01\x01')





_SIMPLESERVICE = descriptor.ServiceDescriptor(
  name='SimpleService',
  full_name='SimpleService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=69,
  serialized_end=147,
  methods=[
  descriptor.MethodDescriptor(
    name='getSimple',
    full_name='SimpleService.getSimple',
    index=0,
    containing_service=None,
    input_type=pbandj_test_pb2._SIMPLE,
    output_type=pbandj_test_pb2._SIMPLE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getSimpler',
    full_name='SimpleService.getSimpler',
    index=1,
    containing_service=None,
    input_type=pbandj_test_pb2._SIMPLE,
    output_type=pbandj_test_pb2._SIMPLE,
    options=None,
  ),
])

class SimpleService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _SIMPLESERVICE
class SimpleService_Stub(SimpleService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _SIMPLESERVICE


_SIMPLERSERVICE = descriptor.ServiceDescriptor(
  name='SimplerService',
  full_name='SimplerService',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=149,
  serialized_end=196,
  methods=[
  descriptor.MethodDescriptor(
    name='simplyGet',
    full_name='SimplerService.simplyGet',
    index=0,
    containing_service=None,
    input_type=pbandj_test_pb2._SIMPLE,
    output_type=pbandj_test_pb2._SIMPLE,
    options=None,
  ),
])

class SimplerService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _SIMPLERSERVICE
class SimplerService_Stub(SimplerService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _SIMPLERSERVICE

# @@protoc_insertion_point(module_scope)