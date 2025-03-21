from typing import Optional

from anemoi.inference.context import Context
from anemoi.inference.decorators import main_argument
from anemoi.inference.output import Output
from anemoi.inference.types import State


class ${plugin_class}(Output):

    api_version = "${api_version}"
    schema = None

    def __init__(
        self,
        context: Context,
        path: str,
        output_frequency: Optional[int] = None,
        write_initial_state: Optional[bool] = None,
    ) -> None:
        super().__init__(
            context,
            output_frequency=output_frequency,
            write_initial_state=write_initial_state,
        )

    def open(self, state: State) -> None:
        pass

    def write_step(self, state: State) -> None:
        pass

    def close(self) -> None:
        pass
