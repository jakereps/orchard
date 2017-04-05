# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


class Argument:
    command = None
    value = None

    def __init__(self, data):
        self.name = data.get('name')
        self.command = data.get('command')
        self.value = data.get('value')

    def add_value(self, value):
        self.value = value

    def __repr__(self):
        return self.name


class Exclusive:
    def __init__(self, arguments):
        self._add_arguments(arguments)
        self.name = '(%s)' % ', '.join([arg.name for arg in self.arguments])

    def _add_arguments(self, arguments):
        self.arguments = []
        for argument in arguments:
            arg = Argument(argument)
            if argument.get('value'):
                arg.add_value(argument['value'])
            self.arguments.append(arg)

    def __repr__(self):
        return self.name
