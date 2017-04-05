# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


class Argument:
    def __init__(self, data):
        self.name = data.get('name')

    def add_value(self, value):
        self.value = value

    def __repr__(self):
        return self.name


class Exclusive:
    def __init__(self, arguments):
        self._add_arguments(arguments)

    def _add_arguments(self, arguments):
        self.arguments = []
        for argument in arguments:
            self.arguments.append(Argument(argument))
