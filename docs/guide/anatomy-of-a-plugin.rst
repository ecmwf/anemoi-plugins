..
   anatomy-of-a-plugin:

#####################
 Anatomy of a Plugin
#####################

A typical plugin will look like this:

.. code:: python

   from pydantic import BaseModel, Field
   from anemoi.package.kind import Kind


   class MyKindSchema(BaseModel):
       param1: str = Field(..., description="A required parameter")
       param2: int = Field(default=6, description="An optional parameter with a default")


   class MyKindPlugin(Kind):

       # The version of the plugin API, used to ensure compatibility
       # with the plugin manager.

       api_version = "1.0.0"

       # The schema of the plugin, used to validate the parameters.
       # This is a Pydantic BaseModel subclass.

       schema = MyKindSchema

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

The ``schema`` attribute is a Pydantic ``BaseModel`` subclass used to
validate the parameters passed to the plugin when they are loaded from
the YAML configuration file. Define a schema class with fields matching
the plugin's ``__init__`` parameters. Required fields use ``...`` as the
default, while optional fields provide a default value. If no schema is
set (``schema = None``), parameters are passed through as a plain
dictionary without validation.
