.. _index-page:

###########################################
 Welcome to Anemoi's plugin documentation!
###########################################

The *Anemoi* packages can be extended with plugins. This documentation
provides examples of how to create plugins.

.. admonition:: When to develop a plugin?

   Anemoi plugins are intended to be developed for features that are
   specific to an organisation. For example, if you want to create
   datasets from your own archived data, encoded using an in-house
   bespoke format, then you should implement an :ref:`anemoi-datasets
   <anemoi-datasets:index-page>` source plugin.

   If you intend to develop an :ref:`anemoi-transform
   <anemoi-transform:index-page>` filter that could be used by many
   users, you should consider contributing it to the main repository.

*******************
 What are plugins?
*******************

Plugins are Python classes that extend the functionality of the *Anemoi*
packages, but are developed and maintained separately. *Anemoi* will
look for plugins that have been installed in the Python environment and
add them to the available functionality:

.. code:: bash

   % pip install anemoi-dataset
   % pip install my-dataset-plugin

*****************
 Getting started
*****************

The following packages can be extended with plugins:

-  :ref:`anemoi-transform <anemoi-transform:index-page>`

   -  Sources
   -  Filters

-  :ref:`anemoi-datasets <anemoi-datasets:index-page>` (create)

   -  :ref:`Sources <anemoi-datasets:sources>`
   -  Filters

-  :ref:`anemoi-inference <anemoi-inference:index-page>`

   -  Inputs
   -  Outputs
   -  Pre-processors
   -  Post-processors
   -  Runners

To get started with creating plugins, it is suggested that you install
this package and run the ``anemoi-plugins new`` :ref:`command
<new_command>` to create a new plugin project.

.. code:: bash

   % pip install anemoi-plugins
   % anemoi-plugins new anemoi.datasets.create.source --name my-source

Then, you can follow the instructions in the :ref:`User Guide
<user-guide-introduction>` to create your plugin.

.. _new_command: https://anemoi.readthedocs.io/en/latest/cli/new/

***********************
 Other Anemoi packages
***********************

-  :ref:`anemoi-utils <anemoi-utils:index-page>`
-  :ref:`anemoi-transform <anemoi-transform:index-page>`
-  :ref:`anemoi-datasets <anemoi-datasets:index-page>`
-  :ref:`anemoi-models <anemoi-models:index-page>`
-  :ref:`anemoi-graphs <anemoi-graphs:index-page>`
-  :ref:`anemoi-training <anemoi-training:index-page>`
-  :ref:`anemoi-inference <anemoi-inference:index-page>`
-  :ref:`anemoi-registry <anemoi-registry:index-page>`
-  :ref:`anemoi-plugins <anemoi-plugins:index-page>`

*********
 License
*********

*Anemoi* is available under the open source `Apache License`__.

.. __: http://www.apache.org/licenses/LICENSE-2.0.html

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: User Guide

   guide/introduction
   guide/anatomy-of-a-plugin

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Examples

   examples/datasets-create-source-basic-source/index
   examples/datasets-create-source-xarray-source/index

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: CLI

   cli/new
