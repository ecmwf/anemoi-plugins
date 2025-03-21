from anemoi.datasets.create.sources.xarray import XarraySourceBase


class ${plugin_class}(XarraySourceBase):
    """A xarray-based source plugin."""

    # The version of the plugin API, used to ensure compatibility
    # with the plugin manager.

    api_version = "${api_version}"

    # The schema of the plugin, used to validate the parameters.
    # This is a Pydantic model.

    schema = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the path or url to the dataset. By default,
        # the superclass initialise it to the value of
        # `path` or `url` found in the kwargs.

        # self.path_or_url = None

        # Dictionnary that will be passed to xarray.open_dataset
        # as kwargs

        self.config = None

        # A dictionnary to help the plugin to extract some
        # of the metadata from the dataset, when it does not follow
        # the CF conventions.

        self.flavour = None

        # A dictionary that can patch some of the variables attributes
        # that are not correctly set in the dataset.

        self.patch = None
