.. _index-page:

###########################################
 Welcome to Anemoi's plugin documentation!
###########################################

The *Anemoi* packages can be extended with plugins. This documentation
provides examples of how to create plugins.

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

*****************
 Getting started
*****************

To get started with creating plugins, it is suggested that you install
this package and run the ``anemoi-plugins new`` :ref:`command
<new_command>` to create a new plugin project.

.. code:: bash

   % pip install anemoi-plugins
   % anemoi-plugins new anemoi.datasets.create.source --name my-source

Then, you can follow the instructions in the :ref:`User Guide
<user-guide-introduction>` to create your plugin.

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
