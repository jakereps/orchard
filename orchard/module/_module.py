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
    dependencies = []

    def __init__(self, module_data, from_link=False):
        self.name = module_data.get('name')
        self.path = module_data.get('path')

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

    def get_command_line_args(self, link_file):
        commands = []
        module_link_data, = filter(lambda x: x.name == self.name,
                                   link_file.modules)
        for argument in self.arguments:
            if isinstance(argument, Argument):
                argument_link_data, = filter(lambda x: x.name == argument.name,
                                             module_link_data.arguments)
                if argument_link_data.command:
                    commands.append(argument_link_data.command)
                commands.append(argument.value)
        return [module_link_data.path, *commands]

    def add_dependency(self, dependency):
        self.dependencies = self.dependencies or []
        self.dependencies.append(dependency)

    def _add_link_values(self, values, dest):
        for value in values:
            if value.get('exclusive'):
                data = value['exclusive']
                dest.append(Exclusive(data))
            else:
                dest.append(Argument(value))

    def _add_config_values(self, values, dest):
        for value in values:
            (name, val), = value.items()
            if name == 'exclusive':
                vals = []
                for arg in val:
                    (key, value), = arg.items()
                    vals.append({'name': key, 'value': value})
                arg = Exclusive(vals)
            else:
                arg = Argument({'name': name, 'value': val})
            dest.append(arg)

    def __repr__(self):
        return '%s: %s' % (self.name, self.arguments)
