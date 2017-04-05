# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import yaml

from ..module import Module


class YAMLFile:
    modules = []

    def __init__(self, filepath):
        with open(filepath) as fh:
            self.data = yaml.load(fh.read())

        for module in self.data.get('modules'):
            self.modules.append(Module(module))
