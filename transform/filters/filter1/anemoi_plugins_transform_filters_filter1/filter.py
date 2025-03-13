#!/usr/bin/env python3
from __future__ import annotations

import logging

# from anemoi.transform.filters import filter_registry
from anemoi.transform.fields import new_field_from_numpy
from anemoi.transform.fields import new_fieldlist_from_list
from anemoi.transform.filter import Filter

LOG = logging.getLogger(__name__)


# if running in a notebook, we need to register the filter
# @filter_registry.register("custom_filter1")
class Custom(Filter):
    """A filter to do something on  fields."""

    def __init__(self, a):
        self.a = a

    def forward(self, data):
        print("✅✅ CustomFilter forward")
        print("  Received data: ")
        for field in data:
            print("  ", field)

        result = []
        for field in data:

            if field.metadata("param") == self.a:
                values = field.to_numpy(flatten=True)
                values = values * 2
                result.append(field)
                result.append(new_field_from_numpy(values, template=field, param=field.metadata("param") + "_modified"))

            else:
                result.append(field)

        return new_fieldlist_from_list(result)

    def backward(self, data):
        raise NotImplementedError()
