import earthkit.data as ekd
from anemoi.transform.filter import Filter


class ${plugin_class}(Filter):
    """A filter to do something on fields."""

    # The version of the plugin API, used to ensure compatibility
    # with the plugin manager.

    api_version = "${api_version}"

    # The schema of the plugin, used to validate the parameters.
    # This is a Pydantic model.

    schema = None

    def __init__(self, factor: float = 2.0):
        """Initialise the filter with the user's parameters"""

        self.factor = factor

    def forward(self, data: ekd.FieldList) -> ekd.FieldList:
        """Multiply all field values by self.factor"""

        result = []
        for field in data: # Loop over all fields in the input data

            values = field.to_numpy() * self.factor # Multiply the field values by self.factor

            out = self.new_field_from_numpy(
                values,
                template=field, # Use the input field as a template for the output field
                param=field.metadata("param") + "_modified", # Add "_modified" to the parameter name
            )

            result.append(out)

        # Return the modified fields
        return self.new_fieldlist_from_list(result)
