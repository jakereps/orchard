# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import tempfile
import unittest

from orchard.file import LinkFile


class TestLinkFile(unittest.TestCase):

    def setUp(self):
        yaml_text = \
            'config:\n' \
            '  pipeline_api_version: 1\n' \
            '  luigi_scheduler_ip: 127.0.0.1\n' \
            '  luigi_scheduler_port: 8082\n' \
            'modules:\n' \
            '- name: ModuleOne\n' \
            '  arguments:\n' \
            '  - name: infile\n' \
            '  - name: outfile\n' \
            '    command: --out\n' \
            '    isBranch: false\n' \
            '  - name: digit\n' \
            '    command: -d\n' \
            '  - exclusive:\n' \
            '    - name: required_exclusive_forward\n' \
            '      command: --required_exclusive_forward\n' \
            '      isFlag: true\n' \
            '    - name: required_exclusive_reverse\n' \
            '      command: --required_exclusive_reverse\n' \
            '      isFlag: true\n'

        self.yaml_file = tempfile.NamedTemporaryFile('w+')
        self.yaml_file.write(yaml_text)
        self.yaml_file.flush()

    def test_creation(self):
        link_file = LinkFile(self.yaml_file.name)

        self.assertIsInstance(link_file, LinkFile)
        self.assertEqual(len(link_file.modules), 1)
