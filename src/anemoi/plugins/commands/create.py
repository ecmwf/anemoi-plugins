# (C) Copyright 2024 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import json
import os
import sys
from argparse import ArgumentParser
from argparse import Namespace
from anemoi.plugins.data import templates_directory, common_directory
from anemoi.utils.mars.requests import print_request

from . import Command


class Create(Command):

    def add_arguments(self, command_parser: ArgumentParser) -> None:
        """Add arguments to the command parser.

        Parameters
        ----------
        command_parser : ArgumentParser
            The argument parser to which the arguments will be added.
        """

        packages = sorted(os.listdir(templates_directory))
        print(packages)
        # for package in os.listdir(templates_directory):
        #     print(templates_directory)

        command_parser.add_argument('package', type=str, help='The package name', choices=packages)
        command_parser.add_argument('kind', type=str, help='The kind of plugin')

    def run(self, args: Namespace) -> None:
        """Execute the command with the provided arguments.

        Parameters
        ----------
        args : Namespace
            The arguments passed to the command.
        """

        target_directory = os.path.join(os.getcwd(), args.package)
        print(f'{target_directory=}')
        print(f'{common_directory=}')

        settings = {
            'package': args.package,
             'package_extended' : args.package + '.create',
            'kind': args.kind,
            'name': 'example',
            'project_name': 'anemoi-package-kind-example-plugin',
            'version': '0.1.0',
            'package_name': 'anemoi_package_kind_example_plugin',
            'entry_point': 'anemoi_package_kind_example_plugin',
            'description': 'An example plugin for the Anemoi package-kind package.',
            'author': 'Anemoi contributors',
            'year': '2024',
            'email': '',
            'url': 'https://anemoi.org',
            'license': 'Apache 2.0',
        }

        self.copy_files(common_directory, target_directory, **settings)



    def copy_files(self, source_directory: str, target_directory: str, **kwargs) -> None:
        """Copy files from the source directory to the target directory.

        Parameters
        ----------
        source_directory : str
            The source directory.
        target_directory : str
            The target directory.
        """
        from mako.template import Template


        for root, _, files in os.walk(source_directory):
            for file in files:
                full = os.path.join(root, file)
                target = os.path.join(target_directory,os.path.relpath(full, source_directory))

                os.makedirs(os.path.dirname(target), exist_ok=True)

                if file.endswith('.mako'):
                    with open(full, 'r') as f:
                        template = Template(f.read())
                        with open(target[:-5], 'w') as g:
                            g.write(template.render(**kwargs))
                else:
                    with open(full, 'r') as f:
                        with open(target, 'w') as g:
                            g.write(f.read())

command = Create
