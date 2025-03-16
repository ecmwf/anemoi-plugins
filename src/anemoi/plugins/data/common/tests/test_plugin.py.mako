from anemoi.${package_extended}.${kind} import create_${kind}
from anemoi.${package_extended}.testing import TestingContext


def test_plugin():
    ${kind} = create_${kind}(TestingContext(), "${name}")


if __name__ == "__main__":
    test_plugin()
