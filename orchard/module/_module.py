# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._argument import Argument, Exclusive


class Module:
    data = None
    optionals = None

    def __init__(self, module_data, from_link=False):
        self.name = module_data.get('name')

        arguments = module_data.get('arguments')
        if arguments:
            self.arguments = []
            if from_link:
                self._add_link_values(arguments, self.arguments)
            else:
                self._add_config_values(arguments, self.arguments)

        optionals = module_data.get('optionals')
        if optionals:
            self.optionals = []
            if from_link:
                self._add_link_values(optionals, self.optionals)
            else:
                self._add_config_values(optionals, self.optionals)

    def add_dependencies(self, dependencies):
        self.dependencies = []
        for dependency in dependencies:
            self.dependencies.append(dependency)

    def _add_link_values(self, values, dest):
        for value in values:
            if 'exclusive' in value:
                data = value['exclusive']
                dest.append(Exclusive(data))
            else:
                dest.append(Argument(value))

    def _add_config_values(self, values, dest):
        for value in values:
            (name, val), = value.items()
            arg = Argument({'name': name})
            arg.add_value(val)
            dest.append(arg)

    def __repr__(self):
        return '%s: %s' % (self.name, self.arguments)
