# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import collections

import yaml

from ..module import Module


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
