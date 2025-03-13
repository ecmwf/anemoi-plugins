####################################
 Welcome to Anemoi's plugin documentation!
####################################

The *Anemoi* packages can be extended with plugins. This documentation provides examples of how to create plugins.

*Anemoi* relies on Python's standard plugin system, based on the `importlib.metadata`_ module.

Add to your `pyproject.toml` file the following lines:

.. code-block:: toml

    [project.entry-points."anemoi.transform.filters"]
    custom_filter = "my.package.filter:CustomFilter"

*****************
 Anemoi packages
*****************

-  :ref:`anemoi-datasets <anemoi-datasets:index-page>`
-  :ref:`anemoi-graphs <anemoi-graphs:index-page>`
-  :ref:`anemoi-inference <anemoi-inference:index-page>`
-  :ref:`anemoi-models <anemoi-models:index-page>`
-  :ref:`anemoi-registry <anemoi-registry:index-page>`
-  :ref:`anemoi-training <anemoi-training:index-page>`
-  :ref:`anemoi-transform <anemoi-transform:index-page>`
-  :ref:`anemoi-utils <anemoi-utils:index-page>`

*********
 License
*********

*Anemoi* is available under the open source `Apache License`__.

.. __: http://www.apache.org/licenses/LICENSE-2.0.html
.. _importlib.metadata: https://docs.python.org/3/library/importlib.html#module-importlib.metadata
