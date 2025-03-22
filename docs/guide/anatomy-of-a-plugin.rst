..
   anatomy-of-a-plugin:

#####################
 Anatomy of a Plugin
#####################

A typical plugin will look like this:

.. code:: python

   from anemoi.package.kind import Kind


   class MyKindPlugin(Kind):

       # The version of the plugin API, used to ensure compatibility
       # with the plugin manager.

       api_version = "1.0.0"

       # The schema of the plugin, used to validate the parameters.
       # This is a Pydantic model.

       schema = None

       def __init__(self, context, param1, param2, *args, **kwargs):
           super().__init__(context, *args, **kwargs)
           self.param1 = param1
           self.param2 = param2

       def overridden_method1(...):
          ...

       def overridden_method2(...):
           ...

In that example ``package``, ``kind`` and ``Kind`` are placeholders for
the actual package, kind and class names.

The ``context`` parameter holds information about the plugin execution
process. Not all the plugins need this parameter. It is given here as an
example of a parameter that needs to be passed to the superclass
constructor.

The ``api_version`` attribute is used to ensure compatibility with the
plugin manager. The plugin manager will check that the plugin API
version is compatible with the plugin manager API version.

The ``schema`` attribute is a Pydantic model that is used to validate
the parameters passed to the plugin, which are loaded from the YAML
configuration file (currently not used).
