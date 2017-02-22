# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click
import yaml


class Setup:

    def __init__(self):
        self.config_data = ConfigDataStore()
        self.link_data = LinkDataStore()

        # TODO: Move to driver/initialize earlier on in the process
        # This is where the link file will be stored on the user's machine
        config_path = click.get_app_dir('orchard', force_posix=True)
        if not os.path.exists(config_path):
            os.mkdir(config_path)


    def _validate(self, config=None, link=None):
        pass

class DataStore:
    pass


class ConfigDataStore(DataStore):
    pass


class LinkDataStore(DataStore):
    pass

if __name__ == '__main__':
    Setup()
