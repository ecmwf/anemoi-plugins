#!/usr/bin/env python3
from __future__ import annotations

import logging

# from anemoi.transform.filters import filter_registry
from anemoi.transform.fields import new_field_from_numpy
from anemoi.transform.filters.matching import MatchingFieldsFilter
from anemoi.transform.filters.matching import matching

LOG = logging.getLogger(__name__)


# if running in a notebook, we need to register the filter
# @filter_registry.register("custom_filter2")
class Custom(MatchingFieldsFilter):
    """A filter to do something on  fields."""

    @matching(
        match=("param"),
        forward=("temperature"),
    )
    def __init__(self, a, temperature="2t"):
        self.a = a
        self.temperature = temperature

    def forward_transform(self, temperature):
        print("✅✅ CustomFilter2 forward_transform")
        print("   Received data: ")
        print("   ", temperature)

        values = temperature.to_numpy(flatten=True)
        values = values * self.a
        new_field = new_field_from_numpy(
            values, template=temperature, param=temperature.metadata("param") + "_modified_2"
        )

        yield temperature
        yield new_field
