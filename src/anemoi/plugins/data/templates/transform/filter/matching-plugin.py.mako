from typing import Any
from typing import Dict
from typing import Iterator

import earthkit.data as ekd
import numpy as np

from anemoi.transform.filters.matching import MatchingFieldsFilter
from anemoi.transform.filters.matching import matching


class ${plugin_class}(MatchingFieldsFilter):
    """A filter to convert mean wave direction to cos() and sin() and back."""

    # The version of the plugin API, used to ensure compatibility
    # with the plugin manager.

    api_version = "${api_version}"

    # The schema of the plugin, used to validate the parameters.
    # This is a Pydantic model.

    schema = None

    @matching(
        select="param",
        forward=("mean_wave_direction",),
        backward=("cos_mean_wave_direction", "sin_mean_wave_direction"),
    )
    def __init__(
        self,
        mean_wave_direction="mwd",
        cos_mean_wave_direction="cos_mwd",
        sin_mean_wave_direction="sin_mwd",
    ) -> None:
        """Initialize the CosSinWaveDirection filter."""

        self.mean_wave_direction = mean_wave_direction
        self.cos_mean_wave_direction = cos_mean_wave_direction
        self.sin_mean_wave_direction = sin_mean_wave_direction

    def forward_transform(
        self,
        mean_wave_direction: ekd.Field,
    ) -> Iterator[ekd.Field]:
        """Convert mean wave direction to its cosine and sine components.

        Parameters
        ----------
        mean_wave_direction : ekd.Field
            The mean wave direction field.

        Returns
        -------
        Iterator[ekd.Field]
            Fields of cosine and sine of the mean wave direction.
        """
        data = mean_wave_direction.to_numpy()
        data = np.deg2rad(data)

        yield self.new_field_from_numpy(np.cos(data), template=mean_wave_direction, param=self.cos_mean_wave_direction)
        yield self.new_field_from_numpy(np.sin(data), template=mean_wave_direction, param=self.sin_mean_wave_direction)

    def backward_transform(
        self,
        cos_mean_wave_direction: ekd.Field,
        sin_mean_wave_direction: ekd.Field,
    ) -> Iterator[ekd.Field]:
        """Convert cosine and sine components back to mean wave direction.

        Parameters
        ----------
        cos_mean_wave_direction : ekd.Field
            The cosine of the mean wave direction field.
        sin_mean_wave_direction : ekd.Field
            The sine of the mean wave direction field.

        Returns
        -------
        Iterator[ekd.Field]
            Field of the mean wave direction.
        """
        mwd = np.rad2deg(np.arctan2(sin_mean_wave_direction.to_numpy(), cos_mean_wave_direction.to_numpy()))
        mwd = np.where(mwd >= 360, mwd - 360, mwd)
        mwd = np.where(mwd < 0, mwd + 360, mwd)

        yield self.new_field_from_numpy(mwd, template=cos_mean_wave_direction, param=self.mean_wave_direction)
