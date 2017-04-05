# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._yaml_file import YAMLFile


class LinkFile(YAMLFile):

    def __init__(self, filepath):
        super().__init__(filepath)
        self.config = self.data.get('config')
