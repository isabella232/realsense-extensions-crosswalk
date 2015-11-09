# Copyright (c) 2015 Intel Corporation. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    # TODO(halton): Hard code of RSSDK_DIR
    #
    # On buildbot, if uses environment variable RSSDK_DIR, the include_dirs
    # and ldflags will be interpreted as relative path, thus fail to compile.
    'rssdk_dir%': 'C:\Program Files (x86)\Intel\RSSDK',
  },
  'include_dirs': [
    '<(rssdk_dir)\include',
    '<(DEPTH)',
  ],
  'dependencies':[
    '<(DEPTH)/base/base.gyp:base',
    '<(DEPTH)/xwalk/common/common.gyp:common',
  ],
  'msvs_settings': {
    'VCLinkerTool': {
      'AdditionalDependencies': [
        'advapi32.lib',
      ],
    },
  },
  'configurations': {
    'Debug': {
      'msvs_settings': {
        'VCLinkerTool': {
          'AdditionalLibraryDirectories': [
            '<(rssdk_dir)\lib\Win32',
          ],
          'AdditionalDependencies': [
            'libpxc_d.lib'
          ],
        },
      },
    },
    'Release': {
      'msvs_settings': {
        'VCLinkerTool': {
          'AdditionalLibraryDirectories': [
            '<(rssdk_dir)\lib\Win32',
          ],
          'AdditionalDependencies': [
            'libpxc.lib'
          ],
        },
      },
    },
    'Debug_x64': {
      'msvs_settings': {
        'VCLinkerTool': {
          'AdditionalLibraryDirectories': [
            '<(rssdk_dir)\\lib\\x64',
          ],
          'AdditionalDependencies': [
            'libpxc_d.lib'
          ],
        },
      },
    },
    'Release_x64': {
      'msvs_settings': {
        'VCLinkerTool': {
          'AdditionalLibraryDirectories': [
            '<(rssdk_dir)\\lib\\x64',
          ],
          'AdditionalDependencies': [
            'libpxc.lib'
          ],
        },
      },
    },
  },
}
