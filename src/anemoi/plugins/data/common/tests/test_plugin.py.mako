from anemoi.${package}.${extended_kind}s import create_${kind}
from anemoi.${package}.${testing} import TestingContext


def test_plugin():
    ${kind} = create_${kind}(TestingContext(), "${name}")
    assert ${kind} is not None

if __name__ == "__main__":
    test_plugin()
