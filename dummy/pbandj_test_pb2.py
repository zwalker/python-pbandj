# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='pbandj_test.proto',
  package='',
  serialized_pb='\n\x11pbandj_test.proto\"r\n\x0cm2massoctest\x12\x1a\n\tsimple_fk\x18\x01 \x01(\x0b\x32\x07.simple\x12\x12\n\nassoc_test\x18\x02 \x01(\x05\x12&\n\x06m2m_fk\x18\x03 \x01(\x0b\x32\x16.manytomanythroughtest\x12\n\n\x02id\x18\x04 \x01(\x05\"\x84\x01\n\x15m2massocrecursiontest\x12\x1a\n\tsimple_fk\x18\x01 \x01(\x0b\x32\x07.simple\x12\x12\n\nassoc_test\x18\x02 \x01(\x05\x12/\n\x06m2m_fk\x18\x03 \x01(\x0b\x32\x1f.manytomanythroughrecursiontest\x12\n\n\x02id\x18\x04 \x01(\x05\"!\n\x06simple\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03val\x18\x02 \x01(\x05\"V\n\x15manytomanythroughtest\x12\x10\n\x08test_val\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x1f\n\x08m2m_test\x18\x03 \x03(\x0b\x32\r.m2massoctest\"h\n\x1emanytomanythroughrecursiontest\x12\x10\n\x08test_val\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12(\n\x08m2m_test\x18\x03 \x03(\x0b\x32\x16.m2massocrecursiontest\"k\n\x17\x63onvolutedrecursiontest\x12\x10\n\x08test_val\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x32\n\x08m2m_test\x18\x03 \x03(\x0b\x32 .convolutedm2massocrecursiontest\"8\n\x0e\x66oreignkeytest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1a\n\tfkey_test\x18\x02 \x01(\x0b\x32\x07.simple\"8\n\x17\x66oreignkeyrecursiontest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tfkey_test\x18\x02 \x01(\x05\"\x9e\x01\n\x1f\x63onvolutedm2massocrecursiontest\x12/\n\x0cm2m_assoc_fk\x18\x01 \x01(\x0b\x32\x19.convolutedforeignkeytest\x12\x1a\n\tsimple_fk\x18\x02 \x01(\x0b\x32\x07.simple\x12\x12\n\nassoc_test\x18\x03 \x01(\x05\x12\x0e\n\x06m2m_fk\x18\x04 \x01(\x05\x12\n\n\x02id\x18\x05 \x01(\x05\"o\n\x08\x65numtest\x12.\n\tenum_test\x18\x01 \x01(\x0e\x32\x1b.enumtest.enum_test_choices\x12\n\n\x02id\x18\x02 \x01(\x05\"\'\n\x11\x65num_test_choices\x12\x08\n\x04val2\x10\x01\x12\x08\n\x04val1\x10\x00\"I\n\x0emanytomanytest\x12\x10\n\x08test_val\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x19\n\x08m2m_test\x18\x03 \x03(\x0b\x32\x07.simple\"g\n\x18\x63onvolutedforeignkeytest\x12\x12\n\nfkey_test2\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12+\n\tfkey_test\x18\x03 \x01(\x0b\x32\x18.convolutedrecursiontest\"\xf4\x03\n\x0foneofeverything\x12\x10\n\x06zfield\x18\x80\x80\x02 \x01(\t\x12\x17\n\rzanotherfield\x18\x81\x80\x02 \x01(\x05\x12\x12\n\nimage_test\x18\x01 \x01(\t\x12\x13\n\x0bsm_int_test\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x11\n\ttime_test\x18\x04 \x01(\t\x12\x12\n\nfloat_test\x18\x05 \x01(\x02\x12\x10\n\x08int_test\x18\x06 \x01(\x05\x12\x0f\n\x07ip_test\x18\x07 \x01(\t\x12\x14\n\x0cpos_int_test\x18\x08 \x01(\r\x12\x16\n\x0e\x66ile_path_test\x18\t \x01(\t\x12\x16\n\x0e\x64\x61te_time_test\x18\n \x01(\t\x12\x10\n\x08url_test\x18\x0b \x01(\t\x12\x11\n\tdate_test\x18\x0c \x01(\t\x12\x17\n\x0fpos_sm_int_test\x18\r \x01(\r\x12\x11\n\tchar_test\x18\x0e \x01(\t\x12\x11\n\tbool_test\x18\x0f \x01(\x08\x12\x16\n\x0enull_bool_test\x18\x10 \x01(\x08\x12\x11\n\ttext_test\x18\x11 \x01(\t\x12\x12\n\nemail_test\x18\x12 \x01(\t\x12\x11\n\tslug_test\x18\x13 \x01(\t\x12\x14\n\x0c\x64\x65\x63imal_test\x18\x14 \x01(\x01\x12\x12\n\ncomma_test\x18\x15 \x01(\t\x12\x11\n\tfile_test\x18\x16 \x01(\tB\x06\x88\x01\x01\x90\x01\x01')



_ENUMTEST_ENUM_TEST_CHOICES = descriptor.EnumDescriptor(
  name='enum_test_choices',
  full_name='enumtest.enum_test_choices',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='val2', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='val1', index=1, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=959,
  serialized_end=998,
)


_M2MASSOCTEST = descriptor.Descriptor(
  name='m2massoctest',
  full_name='m2massoctest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='simple_fk', full_name='m2massoctest.simple_fk', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='assoc_test', full_name='m2massoctest.assoc_test', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_fk', full_name='m2massoctest.m2m_fk', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='m2massoctest.id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=21,
  serialized_end=135,
)


_M2MASSOCRECURSIONTEST = descriptor.Descriptor(
  name='m2massocrecursiontest',
  full_name='m2massocrecursiontest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='simple_fk', full_name='m2massocrecursiontest.simple_fk', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='assoc_test', full_name='m2massocrecursiontest.assoc_test', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_fk', full_name='m2massocrecursiontest.m2m_fk', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='m2massocrecursiontest.id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=138,
  serialized_end=270,
)


_SIMPLE = descriptor.Descriptor(
  name='simple',
  full_name='simple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='simple.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val', full_name='simple.val', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=272,
  serialized_end=305,
)


_MANYTOMANYTHROUGHTEST = descriptor.Descriptor(
  name='manytomanythroughtest',
  full_name='manytomanythroughtest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='test_val', full_name='manytomanythroughtest.test_val', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='manytomanythroughtest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_test', full_name='manytomanythroughtest.m2m_test', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=307,
  serialized_end=393,
)


_MANYTOMANYTHROUGHRECURSIONTEST = descriptor.Descriptor(
  name='manytomanythroughrecursiontest',
  full_name='manytomanythroughrecursiontest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='test_val', full_name='manytomanythroughrecursiontest.test_val', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='manytomanythroughrecursiontest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_test', full_name='manytomanythroughrecursiontest.m2m_test', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=395,
  serialized_end=499,
)


_CONVOLUTEDRECURSIONTEST = descriptor.Descriptor(
  name='convolutedrecursiontest',
  full_name='convolutedrecursiontest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='test_val', full_name='convolutedrecursiontest.test_val', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='convolutedrecursiontest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_test', full_name='convolutedrecursiontest.m2m_test', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=501,
  serialized_end=608,
)


_FOREIGNKEYTEST = descriptor.Descriptor(
  name='foreignkeytest',
  full_name='foreignkeytest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='foreignkeytest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fkey_test', full_name='foreignkeytest.fkey_test', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=610,
  serialized_end=666,
)


_FOREIGNKEYRECURSIONTEST = descriptor.Descriptor(
  name='foreignkeyrecursiontest',
  full_name='foreignkeyrecursiontest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='foreignkeyrecursiontest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fkey_test', full_name='foreignkeyrecursiontest.fkey_test', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=668,
  serialized_end=724,
)


_CONVOLUTEDM2MASSOCRECURSIONTEST = descriptor.Descriptor(
  name='convolutedm2massocrecursiontest',
  full_name='convolutedm2massocrecursiontest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='m2m_assoc_fk', full_name='convolutedm2massocrecursiontest.m2m_assoc_fk', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='simple_fk', full_name='convolutedm2massocrecursiontest.simple_fk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='assoc_test', full_name='convolutedm2massocrecursiontest.assoc_test', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_fk', full_name='convolutedm2massocrecursiontest.m2m_fk', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='convolutedm2massocrecursiontest.id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=727,
  serialized_end=885,
)


_ENUMTEST = descriptor.Descriptor(
  name='enumtest',
  full_name='enumtest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='enum_test', full_name='enumtest.enum_test', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='enumtest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENUMTEST_ENUM_TEST_CHOICES,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=887,
  serialized_end=998,
)


_MANYTOMANYTEST = descriptor.Descriptor(
  name='manytomanytest',
  full_name='manytomanytest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='test_val', full_name='manytomanytest.test_val', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='manytomanytest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='m2m_test', full_name='manytomanytest.m2m_test', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1000,
  serialized_end=1073,
)


_CONVOLUTEDFOREIGNKEYTEST = descriptor.Descriptor(
  name='convolutedforeignkeytest',
  full_name='convolutedforeignkeytest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='fkey_test2', full_name='convolutedforeignkeytest.fkey_test2', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='convolutedforeignkeytest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fkey_test', full_name='convolutedforeignkeytest.fkey_test', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1075,
  serialized_end=1178,
)


_ONEOFEVERYTHING = descriptor.Descriptor(
  name='oneofeverything',
  full_name='oneofeverything',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='zfield', full_name='oneofeverything.zfield', index=0,
      number=32768, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='zanotherfield', full_name='oneofeverything.zanotherfield', index=1,
      number=32769, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='image_test', full_name='oneofeverything.image_test', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sm_int_test', full_name='oneofeverything.sm_int_test', index=3,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='oneofeverything.id', index=4,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_test', full_name='oneofeverything.time_test', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='float_test', full_name='oneofeverything.float_test', index=6,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int_test', full_name='oneofeverything.int_test', index=7,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ip_test', full_name='oneofeverything.ip_test', index=8,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos_int_test', full_name='oneofeverything.pos_int_test', index=9,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_path_test', full_name='oneofeverything.file_path_test', index=10,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='date_time_test', full_name='oneofeverything.date_time_test', index=11,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url_test', full_name='oneofeverything.url_test', index=12,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='date_test', full_name='oneofeverything.date_test', index=13,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos_sm_int_test', full_name='oneofeverything.pos_sm_int_test', index=14,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_test', full_name='oneofeverything.char_test', index=15,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bool_test', full_name='oneofeverything.bool_test', index=16,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='null_bool_test', full_name='oneofeverything.null_bool_test', index=17,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text_test', full_name='oneofeverything.text_test', index=18,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='email_test', full_name='oneofeverything.email_test', index=19,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slug_test', full_name='oneofeverything.slug_test', index=20,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='decimal_test', full_name='oneofeverything.decimal_test', index=21,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comma_test', full_name='oneofeverything.comma_test', index=22,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_test', full_name='oneofeverything.file_test', index=23,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1181,
  serialized_end=1681,
)

_M2MASSOCTEST.fields_by_name['simple_fk'].message_type = _SIMPLE
_M2MASSOCTEST.fields_by_name['m2m_fk'].message_type = _MANYTOMANYTHROUGHTEST
_M2MASSOCRECURSIONTEST.fields_by_name['simple_fk'].message_type = _SIMPLE
_M2MASSOCRECURSIONTEST.fields_by_name['m2m_fk'].message_type = _MANYTOMANYTHROUGHRECURSIONTEST
_MANYTOMANYTHROUGHTEST.fields_by_name['m2m_test'].message_type = _M2MASSOCTEST
_MANYTOMANYTHROUGHRECURSIONTEST.fields_by_name['m2m_test'].message_type = _M2MASSOCRECURSIONTEST
_CONVOLUTEDRECURSIONTEST.fields_by_name['m2m_test'].message_type = _CONVOLUTEDM2MASSOCRECURSIONTEST
_FOREIGNKEYTEST.fields_by_name['fkey_test'].message_type = _SIMPLE
_CONVOLUTEDM2MASSOCRECURSIONTEST.fields_by_name['m2m_assoc_fk'].message_type = _CONVOLUTEDFOREIGNKEYTEST
_CONVOLUTEDM2MASSOCRECURSIONTEST.fields_by_name['simple_fk'].message_type = _SIMPLE
_ENUMTEST.fields_by_name['enum_test'].enum_type = _ENUMTEST_ENUM_TEST_CHOICES
_ENUMTEST_ENUM_TEST_CHOICES.containing_type = _ENUMTEST;
_MANYTOMANYTEST.fields_by_name['m2m_test'].message_type = _SIMPLE
_CONVOLUTEDFOREIGNKEYTEST.fields_by_name['fkey_test'].message_type = _CONVOLUTEDRECURSIONTEST
DESCRIPTOR.message_types_by_name['m2massoctest'] = _M2MASSOCTEST
DESCRIPTOR.message_types_by_name['m2massocrecursiontest'] = _M2MASSOCRECURSIONTEST
DESCRIPTOR.message_types_by_name['simple'] = _SIMPLE
DESCRIPTOR.message_types_by_name['manytomanythroughtest'] = _MANYTOMANYTHROUGHTEST
DESCRIPTOR.message_types_by_name['manytomanythroughrecursiontest'] = _MANYTOMANYTHROUGHRECURSIONTEST
DESCRIPTOR.message_types_by_name['convolutedrecursiontest'] = _CONVOLUTEDRECURSIONTEST
DESCRIPTOR.message_types_by_name['foreignkeytest'] = _FOREIGNKEYTEST
DESCRIPTOR.message_types_by_name['foreignkeyrecursiontest'] = _FOREIGNKEYRECURSIONTEST
DESCRIPTOR.message_types_by_name['convolutedm2massocrecursiontest'] = _CONVOLUTEDM2MASSOCRECURSIONTEST
DESCRIPTOR.message_types_by_name['enumtest'] = _ENUMTEST
DESCRIPTOR.message_types_by_name['manytomanytest'] = _MANYTOMANYTEST
DESCRIPTOR.message_types_by_name['convolutedforeignkeytest'] = _CONVOLUTEDFOREIGNKEYTEST
DESCRIPTOR.message_types_by_name['oneofeverything'] = _ONEOFEVERYTHING

class m2massoctest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M2MASSOCTEST
  
  # @@protoc_insertion_point(class_scope:m2massoctest)

class m2massocrecursiontest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _M2MASSOCRECURSIONTEST
  
  # @@protoc_insertion_point(class_scope:m2massocrecursiontest)

class simple(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLE
  
  # @@protoc_insertion_point(class_scope:simple)

class manytomanythroughtest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANYTOMANYTHROUGHTEST
  
  # @@protoc_insertion_point(class_scope:manytomanythroughtest)

class manytomanythroughrecursiontest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANYTOMANYTHROUGHRECURSIONTEST
  
  # @@protoc_insertion_point(class_scope:manytomanythroughrecursiontest)

class convolutedrecursiontest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONVOLUTEDRECURSIONTEST
  
  # @@protoc_insertion_point(class_scope:convolutedrecursiontest)

class foreignkeytest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOREIGNKEYTEST
  
  # @@protoc_insertion_point(class_scope:foreignkeytest)

class foreignkeyrecursiontest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOREIGNKEYRECURSIONTEST
  
  # @@protoc_insertion_point(class_scope:foreignkeyrecursiontest)

class convolutedm2massocrecursiontest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONVOLUTEDM2MASSOCRECURSIONTEST
  
  # @@protoc_insertion_point(class_scope:convolutedm2massocrecursiontest)

class enumtest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMTEST
  
  # @@protoc_insertion_point(class_scope:enumtest)

class manytomanytest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANYTOMANYTEST
  
  # @@protoc_insertion_point(class_scope:manytomanytest)

class convolutedforeignkeytest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONVOLUTEDFOREIGNKEYTEST
  
  # @@protoc_insertion_point(class_scope:convolutedforeignkeytest)

class oneofeverything(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ONEOFEVERYTHING
  
  # @@protoc_insertion_point(class_scope:oneofeverything)

# @@protoc_insertion_point(module_scope)
