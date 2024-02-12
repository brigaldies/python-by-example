"""
Type hits examples unit tests.
"""
from examples.typehints import type_hints_example as th


def test_type_hints() -> None:
    """
    Test type hints with dictionaries.
    :return: None.
    """
    greetings = th.generate_greetings('bertrand')
    assert greetings is not None
    assert isinstance(greetings, dict)
    assert len(greetings) > 0
    assert greetings.get('morning') is not None
    assert 'good morning bertrand' in greetings['morning'].lower()
