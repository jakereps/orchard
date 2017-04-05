# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from orchard.module import Argument


class TestArguments(unittest.TestCase):
    def setUp(self):
        self.arg_data = [{'name': 'infile'}, {'name': 'outfile'}]
        self.values = ['test1.txt', 'test2.txt']

    def test_creation(self):
        for data in self.arg_data:
            arg = Argument(data)

            self.assertIsInstance(arg, Argument)

    def test_value_addition(self):
        for data, value in zip(self.arg_data, self.values):
            arg = Argument(data)
            arg.add_value(value)

            self.assertEqual(arg.value, value)

    def test_repr(self):
        for data, value in zip(self.arg_data, self.values):
            arg = Argument(data)

            self.assertEqual(str(arg), data.get('name'))


if __name__ == '__main__':
    unittest.main()
