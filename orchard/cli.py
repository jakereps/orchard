# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click

from orchard.core import validate, generate_luigi
from orchard.file import LinkFile, ConfigFile


@click.group()
def orchard():
    pass


@orchard.command()
@click.argument('filepath', type=click.Path(exists=True))
def template(filepath):
    if not filepath.endswith('.yaml'):
        click.secho('Invalid filetype, please provide a .yml or .yaml link '
                    'file', fg='red', err=True)
        click.get_current_context().exit(1)

    try:
        LinkFile(filepath).template_config_file()
    except RuntimeError as e:
        click.secho(str(e), fg='red', err=True)
        click.get_current_context().exit(1)

    click.secho('Successfully wrote config.yaml', fg='green')


@orchard.command()
@click.argument('link_file_path', type=click.Path(exists=True))
@click.argument('config_file_path', type=click.Path(exists=True))
@click.option('-o', '--output', default='out.py')
def build(link_file_path, config_file_path, output):
    if not (link_file_path.endswith('.yaml') or
            config_file_path.endswith('.yaml')):
        click.secho('Invalid filetype, please provide a .yml or .yaml link '
                    'file', fg='red', err=True, bold=True)
        click.get_current_context().exit(1)

    try:
        link_file = LinkFile(link_file_path)
        config_file = ConfigFile(config_file_path)
        if not validate(link_file_path, config_file_path):
            click.secho('Invalid configuration file.', fg='red', err=True)
            click.get_current_context().exit(1)
        generate_luigi(config_file, link_file)
    except (ValueError, RuntimeError) as e:
        click.secho(str(e), fg='red', err=True, bold=True)
        click.get_current_context().exit(1)
