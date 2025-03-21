from typing import List
from typing import Optional

from anemoi.inference.context import Context
from anemoi.inference.input import Input
from anemoi.inference.output import Output
from anemoi.inference.types import Date
from anemoi.inference.types import State


class ${plugin_class}(Input):

    api_version = "${api_version}"
    schema = None

    trace_name = "${name}"

    def __init__(self, context: Context):
        super().__init__(context)

    def create_input_state(self, *, date: Optional[Date]) -> State:
        pass

    def load_forcings_state(
        self, *, variables: List[str], dates: List[Date], current_state: State
    ) -> State:
        pass
