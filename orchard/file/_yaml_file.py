# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import collections

import yaml


class YAMLFile:
    modules = None

    def __init__(self, filepath):
        self.data = collections.defaultdict(list)
        with open(filepath) as fh:
            try:
                self.data.update(yaml.load(fh))
            except Exception as e:
                raise RuntimeError('The link file is not a valid yaml format.')

        modules = self.data.get('modules')
        if modules:
            self.modules = []
            self._add_modules(modules)

    def write(self, data, filepath):
        def _add_repr(dumper, value):
            return dumper.represent_scalar(u'tag:yaml.org,2002:null', '')
        yaml.SafeDumper.add_representer(type(None), _add_repr)

        with open(filepath, 'w') as fh:
            yaml.safe_dump(data, fh, default_flow_style=False)
