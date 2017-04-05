# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._argument import Argument


class Module:

    def __init__(self, module_data):
        self.name = module_data.get('name')

        arguments = module_data.get('arguments')
        if arguments:
            self.add_arguments(arguments)

    def add_dependencies(self, data):
        for dependency in data.get('dependencies', []):
            pass

    def add_arguments(self, arguments):
        self.arguments = []
        for argument in arguments:
            self.arguments.append(Argument(argument))

    def __repr__(self):
        return '%s: %s' % (self.name, self.arguments)
