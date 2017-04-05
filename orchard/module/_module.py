# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._argument import Argument


class Module:

    def __init__(self, module_data, from_link=False):
        self.name = module_data.get('name')

        arguments = module_data.get('arguments')
        if arguments:
            if from_link:
                self._add_link_arguments(arguments)
            else:
                self._add_config_arguments(arguments)

    def add_dependencies(self, dependencies):
        self.dependencies = []
        for dependency in dependencies:
            self.dependencies.append(dependency)

    def _add_link_arguments(self, arguments):
        self.arguments = []
        for argument in arguments:
            self.arguments.append(Argument(argument))

    def _add_config_arguments(self, arguments):
        self.arguments = []
        for argument in arguments:
            (name, value), = argument.items()
            arg = Argument({'name': name})
            arg.add_value(value)
            self.arguments.append(arg)

    def __repr__(self):
        return '%s: %s' % (self.name, self.arguments)
