from anemoi.inference.inputs import create_input
from anemoi.inference.testing import TestingContext


def test_plugin():
    create_input(TestingContext(), "example")


if __name__ == "__main__":
    test_plugin()
