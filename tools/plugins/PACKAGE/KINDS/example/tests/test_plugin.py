from anemoi.PACKAGE.EXTRAKINDs import create_KIND
from anemoi.PACKAGE.EXTRAtesting import TestingContext

def test_plugin():
    KIND = create_KIND(TestingContext(), "example")


if __name__ == "__main__":
    test_plugin()
