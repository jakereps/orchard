# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
#
# usage: from _generator import generate_luigi
# usage cont: generate_luigi("configfilepath", "linkfilepath")
#
# will generate a luigi file named test.py
# ----------------------------------------------------------------------------

import pkg_resources

import jinja2

TEMPLATES = pkg_resources.resource_filename('orchard', '_data')


def generate_luigi(config_file, link_file, dest="out.py"):

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES))
    template = env.get_template('luigi.py.j2')

    skeleton = {'config': config_file, 'link': link_file}
    rendered_content = template.render(skeleton)

    if not dest.endswith('.py'):
        dest += '.py'

    with open(dest, 'w') as fh:
        fh.write(rendered_content)
