import logging

import earthkit.data as ekd
from anemoi.transform.filter import Filter

LOG = logging.getLogger(__name__)


class ${plugin_class}(Filter):
    """A filter to do something on fields."""

    api_version = "${api_version}"
    schema = None

    def __init__(self, factor: float = 2):
        self.factor = factor

    def forward(self, data: ekd.FieldList) -> ekd.FieldList:

        result = []
        for field in data:
            values = field.to_numpy() * self.factor

            out = self.new_field_from_numpy(
                values,
                template=field,
                param=field.metadata("param") + "_modified",
            )

            result.append(out)

        return self.new_fieldlist_from_list(result)
