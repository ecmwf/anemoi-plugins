from anemoi.PACKAGE.KINDs import create_KIND
from anemoi.PACKAGE.testing import TestingContext

def test_plugin():
    KIND = create_KIND(TestingContext(), "example")


if __name__ == "__main__":
    test_plugin()
