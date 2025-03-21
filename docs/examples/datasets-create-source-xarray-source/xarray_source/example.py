import earthkit.data as ekd
from anemoi.datasets.create.sources.xarray import XarraySourceBase


class ExamplePlugin(XarraySourceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, dates) -> ekd.FieldList:
        return None
