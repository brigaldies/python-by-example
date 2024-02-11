from examples.typehints import type_hints_example as th


def test_type_hints():
    greetings = th.generate_greetings('bertrand')
    assert greetings is not None
    assert type(greetings) is dict
    assert len(greetings) > 0
    assert 'morning' in greetings.keys()
    assert 'good morning bertrand' in greetings['morning'].lower()
