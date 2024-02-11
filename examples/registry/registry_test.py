from examples.registry import registry


def test_registry():
    registered_examples = registry.Registry()
    assert registered_examples is not None
    assert registered_examples.is_registered("type-hints")
