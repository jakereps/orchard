# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pkg_resources
import subprocess

import click

from .modules import generate_config_file

TEMPLATES = pkg_resources.resource_filename('orchard', 'data')


@click.group()
def orchard():
    pass


@orchard.command()
@click.argument('filepath', type=click.Path(exists=True))
def template(filepath):
    if not (filepath.endswith('.yml') or filepath.endswith('.yaml')):
        click.secho('Invalid filetype, please provide a .yml or .yaml link '
                    'file', fg='red', err=True)
        click.get_current_context().exit(1)

    try:
        generate_config_file(filepath)
    except RuntimeError as e:
        click.secho(str(e), fg='red', err=True)
        click.get_current_context().exit(1)

    click.secho('Successfully wrote config.yaml', fg='green')


@orchard.command()
@click.argument('filename')
@click.argument('task')
def launch(filename, task):
    subprocess.run(['python', filename, task])


@orchard.command()
@click.argument('config_file')
@click.option('-o', '--output', default='out.py')
def build(config_file, output):
    # TODO Call driver function here
    pass
