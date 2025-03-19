import earthkit.data as ekd

from anemoi.datasets.create.source import Source
from anemoi.datasets.create.typing import DateList


class ${plugin_class}(Source):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, dates: DateList) -> ekd.FieldList:
        return None
