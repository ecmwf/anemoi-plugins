from anemoi.inference.context import Context
from anemoi.inference.types import DataRequest
from anemoi.inference.types import Date
from anemoi.inference.types import State

class ${plugin_class}(Input):


    def create_input_state(self, *, date: Optional[Date]) -> State:
        """Create the input state for the given date.
        pass
