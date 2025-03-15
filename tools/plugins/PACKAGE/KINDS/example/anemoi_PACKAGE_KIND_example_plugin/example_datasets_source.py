from anemoi.PACKAGE.EXTRAKIND import CLASS


class ExamplePlugin(CLASS):
    """An example KIND plugin for anemoi.PACKAGE."""

    def execute(self, dates):
        """Execute the plugin.

        Parameters
        ----------
        dates : GroupOfDates
            The input dates for the plugin.

        Returns
        -------
        ekd.FieldList
            The output data from the plugin.
        """
        return dates
