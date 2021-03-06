# ----------------------------------------------------------------------------
# Copyright (c) 2016--, AGCT development team.
#
# Distributed under the terms of the GPLv3 License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import subprocess

import click
import yaml

from orchard.core import validate, generate_luigi, branching
from orchard.file import LinkFile, ConfigFile


@click.group()
def orchard():
    pass


@orchard.command()
@click.argument('filepath', type=click.Path(exists=True))
def launch(filepath):
    subprocess.run('python %s wrapper' % filepath, shell=True)


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
        config_file = ConfigFile(config_file_path, True)
        if not validate(link_file_path, config_file_path):
            click.secho('Invalid configuration file.', fg='red', err=True)
            click.get_current_context().exit(1)

        config_file = branching(config_file, link_file, os.getcwd())

        def _add_repr(dumper, value):
            return dumper.represent_scalar(u'tag:yaml.org,2002:null', '')

        yaml.SafeDumper.add_representer(type(None), _add_repr)

        with open('blah.yaml', 'w+') as fh:
            yaml.safe_dump(config_file.get_yaml(), fh,
                           default_flow_style=False)

        config_file = ConfigFile('blah.yaml', True)
        generate_luigi(config_file, link_file)
    except (ValueError, RuntimeError) as e:
        click.secho(str(e), fg='red', err=True, bold=True)
        click.get_current_context().exit(1)
