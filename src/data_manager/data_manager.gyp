# Copyright 2010-2013, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'variables': {
    'relative_dir': 'data_manager',
    'gen_out_dir': '<(SHARED_INTERMEDIATE_DIR)/<(relative_dir)',
  },
  'targets': [
    {
      'target_name': 'user_pos_manager',
      'type': 'none',
      'toolsets': [ 'target', 'host' ],
      'sources': [
        'user_pos_manager.h',
      ],
      'dependencies': [
        'oss/oss_data_manager_base.gyp:oss_user_pos_manager',
      ],
      'conditions': [
        ['use_packed_dictionary==1', {
          'dependencies': [
            'packed/packed_data_manager_base.gyp:packed_data_manager'
          ],
          'dependencies!': [
            'oss/oss_data_manager_base.gyp:oss_user_pos_manager'
          ]
        }],
      ],
    },
    {
      'target_name': 'connection_file_reader',
      'type': 'static_library',
      'toolsets': [ 'target', 'host' ],
      'sources': [
        'connection_file_reader.cc',
      ],
      'dependencies': [
        '../base/base.gyp:base',
      ],
    },
  ],
}
