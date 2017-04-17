# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import os
import tempfile
import filecmp

import yaml
from ..file import LinkFile


def validate(link_file_path, config_file_path):
    # Simplify both the link and the config files then compare

    with tempfile.TemporaryDirectory() as tmp:
        link_path = os.path.join(tmp, 'link_test.yaml')
        config_path = os.path.join(tmp, 'config_test.yaml')

        LinkFile(link_file_path).template_config_file(link_path)
        simplify(config_file_path, config_path)

        sameFile = filecmp.cmp(link_path, config_path)

    return sameFile


def simplify(config_file_path, output_file_name):
    to_ignore = ['exclusive', 'optionals']

    with open(config_file_path) as fh:
        dictionary = yaml.load(fh, Loader=yaml.Loader)

    for module in dictionary['modules']:
        name = module.get('name', 'Unknown?')
        for arguments in module.get('arguments', []):
            for key in arguments:
                if key not in to_ignore:
                    if (arguments[key] is None):
                        raise ValueError(
                            "Missing required input argument %s in module: %s."
                            % (key, name))
                    else:
                        arguments[key] = None

            if 'exclusive' in arguments:
                exclusivity_test = False
                for exclusives in arguments.get('exclusive', []):
                    for key in exclusives:
                        if (exclusives[key] is None):
                            pass
                        elif (exclusivity_test):
                            raise ValueError("User provided too many "
                                             "exclusive arguments on %s" % key)
                        else:
                            exclusivity_test = True
                            exclusives[key] = None
                if (not exclusivity_test):
                    raise ValueError("User failed to provide a single "
                                     "exclusive argument")

        for optionals in module.get('optionals', []):
            for key in optionals:
                if key not in to_ignore:
                    optionals[key] = None

            if 'exclusive' in optionals:
                exclusivity_test = False
                for exclusives in optionals.get('exclusive', []):
                    for key in exclusives:
                        if (exclusives[key] is None):
                            pass
                        elif (exclusivity_test):
                            raise ValueError("User provided too many "
                                             "exclusive arguments on %s" % key)
                        else:
                            exclusivity_test = True
                            exclusives[key] = None

    def _add_repr(dumper, value):
        return dumper.represent_scalar(u'tag:yaml.org,2002:null', '')

    yaml.SafeDumper.add_representer(type(None), _add_repr)
    with open(output_file_name, 'w') as fh:
        yaml.safe_dump(dictionary, fh, default_flow_style=False)
