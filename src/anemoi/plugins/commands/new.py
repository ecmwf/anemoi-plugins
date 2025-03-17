# (C) Copyright 2024 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os
from argparse import ArgumentParser
from argparse import Namespace

from anemoi.plugins.data import common_directory
from anemoi.plugins.data import templates_directory

from . import Command

XARRAY = ["datasets.create.source"]
GRIB = ["datasets.create.source", "inference.input"]


class Create(Command):
    """Create a new plugin."""

    def add_arguments(self, command_parser: ArgumentParser) -> None:
        """Add arguments to the command parser.

        Parameters
        ----------
        command_parser : ArgumentParser
            The argument parser to which the arguments will be added.
        """

        packages = sorted(os.listdir(templates_directory))
        kinds = sorted([f"{p}.{k}" for p in packages for k in sorted(os.listdir(os.path.join(templates_directory, p)))])

        command_parser.add_argument("plugin", type=str, help="The type of plugin", choices=kinds)
        group = command_parser.add_mutually_exclusive_group()
        group.add_argument("--xarray", action="store_true", help="Create an xarray plugin")
        group.add_argument("--grib", action="store_true", help="Create a grib plugin")

    def run(self, args: Namespace) -> None:
        """Execute the command with the provided arguments.

        Parameters
        ----------
        args : Namespace
            The arguments passed to the command.
        """

        package, extended_kind = args.plugin.split(".", 1)



        kind = extended_kind.split(".")[-1]
        if extended_kind != kind:
            testing = extended_kind.split(".")[0] + '.testing'
        else:
            testing = 'testing'

        name = "example"

        project_name = f"anemoi-{package}-{extended_kind.replace('.','-')}-example-plugin"
        target_directory = os.path.join(os.getcwd(), 'tmp', package, *extended_kind.split('.'), name)

        plugin_package = project_name.replace("-", "_")
        entry_point = ".".join(["anemoi", package, extended_kind]) + 's'
        plugin_class = name.capitalize() + "Plugin"

        settings: dict = dict(
            package=package,
            kind=kind,
            extended_kind=extended_kind,
            name=name,
            project_name=project_name,
            plugin_package=plugin_package,
            entry_point=entry_point,
            plugin_class=plugin_class,
            testing=testing,
        )

        self.copy_files(
            common_directory,
            target_directory,
            **settings,
        )

        def rename(path: str) -> str:
            """Rename the file if it matches certain criteria.

            Parameters
            ----------
            path : str
                The original file path.

            Returns
            -------
            str
                The renamed file path.
            """
            if path == "plugin.py":
                return f"{name}.py"
            return path

        def specialise(path: str) -> str:
            """Specialise the file if it matches certain criteria.

            Parameters
            ----------
            path : str
                The original file path.

            Returns
            -------
            str
                The specialised file path.
            """

            directory, file = os.path.split(path)
            if args.xarray:
                 specialised_path = os.path.join(directory, "xarray-" + file)
                 if os.path.exists(specialised_path):
                    return specialised_path

            return path

        self.copy_files(
            os.path.join(templates_directory, package, extended_kind),
            os.path.join(target_directory, plugin_package),
            rename=rename,
            specialise=specialise,
            **settings,
        )

    def copy_files(
        self,
        source_directory: str,
        target_directory: str,
        rename: callable = lambda x: x,
        specialise: callable = lambda x: x,
        **kwargs: str,
    ) -> None:
        """Copy files from the source directory to the target directory.

        Parameters
        ----------
        source_directory : str
            The source directory.
        target_directory : str
            The target directory.
        rename : callable, optional
            A function to rename files, by default lambda x: x
        kwargs : str
            Additional keyword arguments to be used in the template rendering.
        """
        from mako.template import Template

        for root, _, files in os.walk(source_directory):
            for file in files:

                if '-' in file:
                    # Skip specialised files
                    continue

                full = os.path.join(root, file)
                target = os.path.join(target_directory, os.path.relpath(full, source_directory))

                os.makedirs(os.path.dirname(target), exist_ok=True)

                full = specialise(full)

                if file.endswith(".mako"):
                    target_name = os.path.splitext(os.path.basename(target))[0]
                    target_dir = os.path.dirname(target)

                    target_name = rename(target_name)
                    target = os.path.join(target_dir, target_name)

                    print(f"Creating {target}")

                    with open(full, "r") as f:
                        template = Template(f.read())
                        with open(target, "w") as g:
                            g.write(template.render(**kwargs))
                else:
                    print(f"Creating {target}")
                    with open(full, "r") as f:
                        with open(target, "w") as g:
                            g.write(f.read())


command = Create
