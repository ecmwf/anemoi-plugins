from anemoi.datasets.create.sources import create_source
from anemoi.datasets.create.testing import TestingContext


def test_plugin():
    source = create_source(TestingContext(), "example")
    assert source is not None


if __name__ == "__main__":
    test_plugin()
