# (C) Copyright 2024 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os
from argparse import ArgumentParser
from argparse import Namespace
from collections import defaultdict

from anemoi.plugins.data import common_directory
from anemoi.plugins.data import templates_directory

from . import Command


class Create(Command):
    """Create a new plugin."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialise the command."""
        super().__init__(*args, **kwargs)

        self.packages = sorted(os.listdir(templates_directory))
        self.kinds = sorted(
            [f"{p}.{k}" for p in self.packages for k in sorted(os.listdir(os.path.join(templates_directory, p)))]
        )

        self.specialisations = dict()

        for kind in self.kinds:
            for root, _, files in os.walk(os.path.join(templates_directory, *kind.split(".", 1))):
                for file in files:
                    if "-" in file:
                        specialisation, file = file.split("-")
                        self.specialisations.setdefault(kind, defaultdict(list))
                        self.specialisations[kind][specialisation].append(file)

    def add_arguments(self, command_parser: ArgumentParser) -> None:
        """Add arguments to the command parser.

        Parameters
        ----------
        command_parser : ArgumentParser
            The argument parser to which the arguments will be added.
        """

        packages = sorted(os.listdir(templates_directory))
        kinds = sorted([f"{p}.{k}" for p in packages for k in sorted(os.listdir(os.path.join(templates_directory, p)))])

        command_parser.add_argument("plugin", type=str, help="The type of plugin", choices=kinds, metavar="PLUGIN")

        command_parser.add_argument("--name", type=str, help="The name of the plugin", default="example")
        command_parser.add_argument("--package", type=str, help="The package of the plugin")

        specialisations = set()
        for s in self.specialisations.values():
            specialisations.update(s.keys())

        command_parser.add_argument(
            "--specialisation",
            type=str,
            help="Specialise plugin",
            choices=sorted(s),
        )

        group = command_parser.add_mutually_exclusive_group()

        group.add_argument("--path", type=str, help="Output directory", default=".")
        group.add_argument("--doc", action="store_true", help="Generate doc examples")
        group.add_argument("--examples", action="store_true", help="Generate examples")

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
            testing = extended_kind.split(".")[0] + ".testing"
        else:
            testing = "testing"

        name = args.name

        if args.package:
            project_name = args.package
            if "." in project_name:
                raise ValueError(f"Invalid package name {project_name}")
        else:
            project_name = f"anemoi-{package}-{extended_kind.replace('.','-')}-example-plugin"

        if args.specialisation:
            self.specialisations.setdefault(args.plugin, defaultdict(list))
            if args.specialisation not in self.specialisations[args.plugin]:
                raise ValueError(f"Specialisation `{args.specialisation}` not found for `{args.plugin}`")

        if args.examples:
            target_directory = os.path.join(args.path, package, *extended_kind.split("."), name)
        elif args.doc:
            top = __file__
            assert "/src/" in top

            while os.path.basename(top) != "src":
                top = os.path.dirname(top)

            top = os.path.join(os.path.dirname(top), "docs", "examples")

            slug = "-".join([package, *extended_kind.split("."), project_name])

            rst = os.path.join(top, slug, "index.rst")
            os.makedirs(os.path.dirname(rst), exist_ok=True)

            target_directory = os.path.join(top, slug)

            if not os.path.exists(rst):
                with open(rst, "w") as f:
                    f.write(f".. _{project_name}:\n\n")
                    f.write(f"{project_name}\n")
                    f.write("=" * len(project_name) + "\n\n")

                    f.write(f".. literalinclude:: {project_name.replace('-', '_')}/{name}.py\n")

        else:
            target_directory = os.path.join(args.path, project_name)

        plugin_package = project_name.replace("-", "_")
        entry_point = ".".join(["anemoi", package, extended_kind]) + "s"
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
            api_version="1.0.0",
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

            if args.specialisation:
                self.specialisations.setdefault(args.plugin, defaultdict(list))
                files = self.specialisations[args.plugin][args.specialisation]
                if file in files:
                    specialised_path = os.path.join(directory, args.specialisation + "-" + file)
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
        specialise : callable, optional
            A function to specialise files, by default lambda x: x
        kwargs : str
            Additional keyword arguments to be used in the template rendering.
        """
        from mako.template import Template

        for root, _, files in os.walk(source_directory):
            for file in files:

                if "-" in file:
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
