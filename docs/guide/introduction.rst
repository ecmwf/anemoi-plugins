.. _user-guide-introduction:

##############
 Introduction
##############

Plugins are a way to extend the functionality of the *Anemoi* packages.

*Anemoi* heavily relies on the `factory pattern
<https://en.wikipedia.org/wiki/Factory_method_pattern>`_ when loaded
YAML configuration files such as `anemoi-datasets` :ref:`recipes
<anemoi-datasets:building-introduction>` or `anemoi-inference` :ref:`run
configuration files <anemoi-inference:api_level3>`.

For examples, the following is a snippet from a `anemoi-datasets` recipe
file, used to build a dataset from a source calles ``my-source``:

.. code:: yaml

   dates:
       start: 2020-01-01
       end: 2020-12-31

   input:
     my-source:
       param1: value1
       param2: value2

*Anemoi* will look for a plugin that implements the ``my-source``
source, or a built-in source that implements it. If both are found, the
plugin will be used.

The Python class that implements the source must be a subclass of the
`Source` class, which is defined in the `anemoi-datasets` package. The
plugin will be instantiated with the parameters ``param1`` and
``param2``. In this examples, the code of the plugin will be as follows:

.. code:: python

   from anemoi.datasets.create import Source


   class MySource(Source):
       def __init__(self, context, param1, param2):
           super().__init__(context)

           self.param1 = param1
           self.param2 = param2

       def execute(self, dates: DateList) -> ekd.FieldList:
           return ...

The ``context`` parameter that hold information about the dataset
creating process, and the ``execute`` method that will be called with
batches of dates. The method must return a list of `earthkit-data
<https://earthkit-data.readthedocs.io>`_ fields.

The examples above is a simple example of a plugin that implements a
`anemoi-dataset` source. Other plugins can be created to implement
filters, inputs, outputs, pre-processors, post-processors, and runners,
and they will have to inherit from the corresponding classes, and
implement the corresponding methods.

For example, two `anemoi-inference` plugins that implements an input and
output will have to inherit from the `Input` class and `Output` class
respectivaly, and may be used as follows:

.. code:: yaml

   checkpoint: /path/to/checkpoint.chkpt

   input:
     my-input:
       path: /path/to/input

   output:
     my-output:
       path: /path/to/output

.. note::

   Although this documentation shows how to package plugins into their
   own Python packages, it is also possible to to bundle several plugins
   of a different type into a single package.

*Anemoi* relies on Python's standard plugin system, based on the
importlib.metadata_ module. Plugins are `entrypoints` that are defined
in the ``pyproject.toml`` file of the plugin package. The entrypoints
are defined as follows:

.. code:: toml

   "entry-points."anemoi.inference.input".my-input = "my_input_package.plugin:MyInputPlugin"

This will defined an `input` plugin that can be used in the
`anemoi-inference` package, and that will be implemented by the
``MyInputPlugin`` class in the ``my_input_package`` package, in the
``plugin.py`` file, and will be available as ``my-input``.

You can use the ``anemoi-plugins new`` :ref:`command <new_command>` to
create a new plugin project. The command will create a new Python
package with the necessary structure to create a plugin. The command
will also create a ``pyproject.toml`` file with the necessary
entrypoints.

.. _importlib.metadata: https://docs.python.org/3/library/importlib.html#module-importlib.metadata
