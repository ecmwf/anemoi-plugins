from anemoi.datasets.create.sources.xarray import XarraySource
import earthkit.data as ekd


class ${plugin_class}(XarraySource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, dates) -> ekd.FieldList:
        return None
