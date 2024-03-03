"""
Type hits examples unit tests.
"""
from examples.typehints.type_hints_examples import generate_greetings


def test_type_hints() -> None:
    """
    Test type hints with dictionaries.
    :return: None.
    """
    greetings = generate_greetings('bertrand')
    assert greetings is not None
    assert isinstance(greetings, dict)
    assert len(greetings) > 0
    assert greetings.get('morning') is not None
    assert 'good morning bertrand' in greetings['morning'].lower()
