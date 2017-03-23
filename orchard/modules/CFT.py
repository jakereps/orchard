# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import yaml


def generate_config_file(link_file_path):
    to_remove = ['isBranch', 'command', 'optional', 'isFlag']

    with open(link_file_path) as fh:
        try:
            dictionary = yaml.load(fh)
        except Exception as e:
            raise RuntimeError('The link file is not a valid yaml format.')

    for modules in dictionary['modules']:
        for item in ['dependencies', 'exclusive']:
            modules.pop(item, None)

        for arguments in modules.get('arguments', []):
            arguments[arguments['name']] = None
            arguments.pop('name')
            for item in to_remove:
                arguments.pop(item, None)

        for optionals in modules.get('optionals', []):
            optionals[optionals['name']] = None
            optionals.pop('name')
            for item in to_remove:
                optionals.pop(item, None)

    def _add_repr(dumper, value):
        return dumper.represent_scalar(u'tag:yaml.org,2002:null', '')

    yaml.SafeDumper.add_representer(type(None), _add_repr)

    with open("config.yaml", 'w') as fh:
        yaml.safe_dump(dictionary, fh, default_flow_style=False)
