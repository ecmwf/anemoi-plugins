from anemoi.datasets.create.sources.xarray import XarraySourceBase
import earthkit.data as ekd


class ${plugin_class}(XarraySourceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, dates) -> ekd.FieldList:
        return None
