.. _new_command:

New Command
===========

.. warning::

    This command in in development and not all the plugins types are implemented yet.

The ``new`` command is used to create a new plugin project.

.. code-block:: bash

    % anemoi-plugins new PLUGIN_TYPE --name PLUGIN_NAME

Plugin types are:

    -  ``datasets.create.filter``
    -  ``datasets.create.source``
    -  ``inference.input``
    -  ``inference.output``
    -  ``inference.post-processor``
    -  ``inference.pre-processor``
    -  ``inference.runner``
    -  ``transform.filter``
    -  ``transform.source``


The command will create a new Python package with the necessary structure to create a plugin. The command will also create a ``pyproject.toml`` file with the necessary entrypoints,
a README file and a test file.

.. code-block:: text

    ─── PROJECT-NAME
        ├── README.md
        ├── pyproject.toml
        ├── tests
        │   └── test_plugin.py
        └── PACKAGE-NAME
            └── PLUGIN-NAME.py

Where ``PROJECT-NAME`` is the name of the project, ``PACKAGE-NAME`` is the name of the package and ``PLUGIN-NAME`` is the name of the plugin.
``PROJECT-NAME`` and ``PACKAGE-NAME`` are the same by default, the first one
uses hiphen-case and the second one uses snake_case.

By default, the plugin class will inherit from the corresponding class of the plugin type.
In some cases, there already exists some spetialised subclasses that can be used instead.
For example, the ``anemoi.datasets.create.source`` can be spetialised to support
Xarray-based sources. You can select the specialisation with the ``--specialisation xarray`` option.


Command description
-------------------

.. argparse::
    :module: anemoi.plugins.__main__
    :func: create_parser
    :prog: anemoi-plugins
    :path: new
