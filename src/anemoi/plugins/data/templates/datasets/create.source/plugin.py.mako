import earthkit.data as ekd

from anemoi.datasets.create.source import Source
from anemoi.datasets.create.typing import DateList


class ${plugin_class}(Source):

    # The version of the plugin API, used to ensure compatibility
    # with the plugin manager.

    api_version = "${api_version}"

    # The schema of the plugin, used to validate the parameters.
    # This is a Pydantic model.

    schema = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, dates: DateList) -> ekd.FieldList:
        # You need to implement this method
        return None
